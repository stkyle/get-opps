
import httpx
from ratelimit import limits
from tenacity import retry, stop_after_attempt, wait_fixed
from cachetools import cached, TTLCache
from .models import Opportunity, OpportunitiesFilter
from .exceptions import OpportunitiesAPIException, RateLimitExceededException, UnauthorizedAccessException, GeneralAPIException
from .transformations import transform_request_filter, transform_response_opportunities
import logging

class OpportunitiesAPIClient:
    PRODUCTION_URL = "https://api.sam.gov/opportunities/v2/search"
    ALPHA_URL = "https://api-alpha.sam.gov/opportunities/v2/search"
    _cache = TTLCache(maxsize=100, ttl=300)

    def __init__(self, api_key: str, base_url: str = PRODUCTION_URL, calls_per_second: int = 10):
        self.logger = logging.getLogger(__name__)
        self.api_key = api_key
        self.base_url = base_url
        self.calls_per_second = calls_per_second
        self.logger.info(f"Initialized API client with base URL: {base_url}")

    # ... other methods ...

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
