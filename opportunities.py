# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:18:35 2023

@author: steve
"""
import os
import httpx
import configparser
from dotenv import load_dotenv
from cachetools import cached, TTLCache
from ratelimit import limits
from tenacity import retry, stop_after_attempt, wait_fixed
from typing import List, Dict, Optional
from pydantic import BaseModel


# Custom Exceptions
class OpportunitiesAPIException(Exception):
    """Base exception class for all Opportunities API errors."""


class RateLimitExceededException(OpportunitiesAPIException):
    """Exception raised when the rate limit is exceeded."""


class UnauthorizedAccessException(OpportunitiesAPIException):
    """Exception raised when unauthorized access is detected."""


class GeneralAPIException(OpportunitiesAPIException):
    """General exception for other API-related errors."""


# Data Models
class Opportunity:
    def __init__(self, title: str, description: str):  # Include other fields as needed
        self.title = title
        self.description = description

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Opportunity':
        return cls(
            title=data['title'],
            description=data['description']
            # ... other fields
        )


class OpportunitiesFilter(BaseModel):
    filter: Optional[str]
    page: Optional[int]
    # ... other fields as needed


# API Client
class OpportunitiesAPIClient:
    PRODUCTION_URL = "https://api.sam.gov/opportunities/v2/search"
    ALPHA_URL = "https://api-alpha.sam.gov/opportunities/v2/search"
    _cache = TTLCache(maxsize=100, ttl=300)

    def __init__(self, api_key: str, base_url: str = PRODUCTION_URL, calls_per_second: int = 10):
        self.api_key = api_key
        self.base_url = base_url
        self.calls_per_second = calls_per_second

    @classmethod
    def from_config_file(cls, config_file_path: str):
        config = configparser.ConfigParser()
        config.read(config_file_path)
        api_key = config['API']['api_key']
        base_url = config['API']['base_url']
        calls_per_second = int(config['API']['calls_per_second'])
        return cls(api_key, base_url, calls_per_second)

    @classmethod
    def from_env_variables(cls):
        load_dotenv()
        api_key = os.getenv('API_KEY')
        base_url = os.getenv('BASE_URL', cls.PRODUCTION_URL)
        calls_per_second = int(os.getenv('CALLS_PER_SECOND', 10))
        return cls(api_key, base_url, calls_per_second)

    @limits(calls=calls_per_second, period=1)
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    @cached(cache=_cache)
    async def get_opportunities_async(self, filter: Optional[OpportunitiesFilter] = None) -> List[Opportunity]:
        params = filter.dict() if filter else None
        headers = {"Authorization": f"Bearer {self.api_key}"}
        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url, params=params, headers=headers)

            # Handle specific error cases
            if response.status_code == 429:
                raise RateLimitExceededException("Rate limit exceeded")
            elif response.status_code == 401:
                raise UnauthorizedAccessException("Unauthorized access")
            elif response.status_code >= 400:
                raise GeneralAPIException(f"API error: {response.text}")

            opportunities = [Opportunity.from_dict(item) for item in response.json()['items']]
            return opportunities

    def clear_cache(self):
        self._cache.clear()

    # Additional methods for pagination, CLI, etc., can be added as needed


# Sample usage:
# client = OpportunitiesAPIClient.from_env_variables()
# filter = OpportunitiesFilter(filter="value")
# opportunities = await client.get_opportunities_async(filter=filter)

