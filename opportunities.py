# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:18:35 2023

@author: steve
"""
import requests
import logging
import time
from typing import Optional, Dict, Any, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OpportunitiesAPIClient:
    PRODUCTION_URL = "https://api.sam.gov/opportunities/v2/search"
    ALPHA_URL = "https://api-alpha.sam.gov/opportunities/v2/search"

    def __init__(self, api_key: str, base_url: str = PRODUCTION_URL, rate_limit: int = 10):
        """Initialize the API client with the API key, base URL, and rate limit."""
        self.api_key = api_key
        self.base_url = base_url
        self.rate_limit = rate_limit
        self.last_request_time = 0

    def _rate_limit(self):
        """Enforce rate limiting by sleeping if necessary."""
        elapsed_time = time.time() - self.last_request_time
        if elapsed_time < 1 / self.rate_limit:
            time.sleep(1 / self.rate_limit - elapsed_time)
        self.last_request_time = time.time()

    def get_opportunities(self, params: Optional[Dict[str, Any]] = None) -> List['Opportunity']:
        """
        Fetch opportunities based on filters using the /v2/search endpoint.

        :param params: A dictionary containing query parameters for filtering opportunities.
        :return: A list of Opportunity objects containing the response data.
        """
        # Apply rate limiting
        self._rate_limit()

        # Headers including the API key for authentication
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            # Performing the GET request with optional query parameters and headers
            response = requests.get(self.base_url, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            logger.error(f"Request error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise

        # Parsing the opportunities into Opportunity objects
        opportunities = [Opportunity.from_dict(item) for item in data['items']]
        return opportunities

class Opportunity:
    def __init__(self, title: str, description: str, ...):  # Include other fields as needed
        self.title = title
        self.description = description
        # ...

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Opportunity':
        """Create an Opportunity object from a dictionary."""
        return cls(
            title=data['title'],
            description=data['description'],
            # ... other fields
        )

# Sample usage with the production server (replace "your_api_key" with the actual API key)
api_client = OpportunitiesAPIClient(api_key="your_api_key")
opportunities = api_client.get_opportunities(params={"filter": "value"})
