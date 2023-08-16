
import pytest
from opportunities_api.client import OpportunitiesAPIClient
from opportunities_api.exceptions import OpportunitiesAPIException

def test_get_opportunities():
    client = OpportunitiesAPIClient(api_key="dummy_key")

    # Expecting an exception since the API key is invalid
    with pytest.raises(OpportunitiesAPIException):
        client.get_opportunities()
