
import pytest
from opportunities_api.models import Opportunity, OpportunitiesFilter

def test_opportunity_model():
    data = {
        "id": "123",
        "title": "Test Opportunity",
        "description": "A test description",
    }
    opportunity = Opportunity(**data)
    assert opportunity.id == "123"
    assert opportunity.title == "Test Opportunity"
    assert opportunity.description == "A test description"

def test_opportunities_filter_model():
    filter_obj = OpportunitiesFilter(filter="keyword", page=1)
    assert filter_obj.filter == "keyword"
    assert filter_obj.page == 1
