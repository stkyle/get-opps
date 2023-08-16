# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:18:35 2023

@author: steve
"""
from typing import Optional
import httpx
from tenacity import retry, stop_after_attempt, wait_fixed
from ratelimit import limits, RateLimitException
from opportunities_api.models import OpportunitiesFilter, Opportunity
from opportunities_api.exceptions import OpportunitiesAPIException
from opportunities_api.transformations import transform_opportunity
from opportunities_api.utils import handle_pagination
import logging

class OpportunitiesAPIClient:
    PRODUCTION_SERVER = "https://api.sam.gov/opportunities/v2/search"
    ALPHA_SERVER = "https://api-alpha.sam.gov/opportunities/v2/search"

    def __init__(self, api_key: str, server: str = PRODUCTION_SERVER):
        self.api_key = api_key
        self.server = server
        self.logger = logging.getLogger(__name__)
    
    @limits(calls=5, period=60)
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _make_request(self, url: str, params: Optional[dict] = None) -> dict:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = httpx.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            self.logger.error(f"HTTP Status Error: {e}")
            raise OpportunitiesAPIException(str(e))
        except RateLimitException:
            self.logger.warning("Rate limit exceeded")
            raise OpportunitiesAPIException("Rate limit exceeded")

    def get_opportunities(self, filters: Optional[OpportunitiesFilter] = None) -> list[Opportunity]:
        url = f"{self.server}/opportunities"
        params = handle_pagination(page=filters.page, size=filters.size) if filters else None
        data = self._make_request(url, params=params)
        return [transform_opportunity(item) for item in data.get("items", [])]

    def transform_request_filter(self, filter: OpportunitiesFilter):
        # Transformation logic here
        return transform_request_filter(filter)

    def transform_response_opportunities(self, response_data):
        # Transformation logic here
        return transform_response_opportunities(response_data)

    @limits(calls=calls_per_second, period=1)
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    @cached(cache=_cache)
    async def get_opportunities_async(self, filter: Optional[OpportunitiesFilter] = None):
        if filter:
            params = self.transform_request_filter(filter)
        else:
            params = None

        # ... existing code ...

        opportunities = self.transform_response_opportunities(response.json())
        return opportunities

    # ... other methods ...
