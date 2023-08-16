from opportunities_api.client import OpportunitiesAPIClient
from opportunities_api.models import OpportunitiesFilter
from opportunities_api.exceptions import OpportunitiesAPIException

# Define your API key
API_KEY = "YOUR_API_KEY_HERE"

# Initialize the client
client = OpportunitiesAPIClient(api_key=API_KEY)

# Fetch opportunities without filters
try:
    opportunities = client.get_opportunities()
    print("Opportunities without filters:", opportunities)
except OpportunitiesAPIException as e:
    print("An error occurred:", e)

# Fetch opportunities with filters
filters = OpportunitiesFilter(filter="keyword", page=1)
try:
    filtered_opportunities = client.get_opportunities(filters=filters)
    print("Opportunities with filters:", filtered_opportunities)
except OpportunitiesAPIException as e:
    print("An error occurred:", e)

# You can also use async methods for asynchronous calls
# Refer to client.get_opportunities_async() and other async methods
