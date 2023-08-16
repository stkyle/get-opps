
from typing import List, Optional
from pydantic import BaseModel

class Opportunity(BaseModel):
    # Define the fields and their types as per the Opportunity object
    id: str
    title: str
    description: str
    # ... other fields ...

    @classmethod
    def from_dict(cls, data: dict) -> 'Opportunity':
        return cls(**data)

class OpportunitiesFilter(BaseModel):
    # Define the fields for the filter object
    filter: Optional[str] = None
    page: Optional[int] = None
    # ... other fields ...
