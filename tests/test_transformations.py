
import pytest
from opportunities_api.transformations import transform_opportunity

def test_transform_opportunity():
    data = {
        "id": "123",
        "title": "Test Opportunity",
        "description": "A test description",
    }
    transformed_data = transform_opportunity(data)
    assert transformed_data["id"] == "123"
    assert transformed_data["title"] == "Test Opportunity"
    assert transformed_data["description"] == "A test description"
