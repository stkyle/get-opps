
import pytest
from opportunities_api.exceptions import OpportunitiesAPIException

def test_opportunities_api_exception():
    try:
        raise OpportunitiesAPIException("Test error message")
    except OpportunitiesAPIException as e:
        assert str(e) == "Test error message"
