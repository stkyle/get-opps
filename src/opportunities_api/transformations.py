
from typing import Dict, Any
from .models import OpportunitiesFilter

def transform_request_filter(filter: OpportunitiesFilter) -> Dict[str, Any]:
    # Example transformation logic
    transformed_filter = {
        "searchFilter": filter.filter,
        "pageNumber": filter.page,
        # ... other transformations ...
    }
    return transformed_filter

def transform_response_opportunities(response_data: Dict[str, Any]) -> list:
    # Example transformation logic
    opportunities = [Opportunity.from_dict(item) for item in response_data['items']]
    return opportunities
