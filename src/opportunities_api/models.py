# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:18:35 2023

@author: steve
"""
from typing import List, Optional
from pydantic import BaseModel, Field

class Opportunity(BaseModel):
    title: str
    solNum: str
    noticeId: str
    noticeType: str
    responseDeadLine: str
    classificationCode: str
    naicsCode: str
    setAside: str
    agency: str
    office: str
    location: str
    postedDate: str
    baseType: str
    archiveType: str
    archiveDate: str
    type: str
    baseId: str
    # ... other fields ...

    @classmethod
    def from_dict(cls, data: dict) -> 'Opportunity':
        return cls(**data)

class OpportunitiesFilter(BaseModel):
    filter: Optional[str] = None
    page: Optional[int] = None
    size: Optional[int] = None
    sort_by: Optional[str] = None
    order: Optional[str] = None

class RequestParameters(BaseModel):
    """
    Represents the request parameters for querying the Opportunities API.
    """

    ptype: Optional[str] = Field(None, description="Enter Procurement type.")
    noticeid: Optional[str] = Field(None, description="Enter Notice Id.")
    solnum: Optional[str] = Field(None, description="Enter Solicitation number.")
    title: Optional[str] = Field(None, description="Enter Title.")
    state: Optional[str] = Field(None, description="Enter Place of performance State.")
    zip: Optional[str] = Field(None, description="Enter Place of performance Zip.")
    typeOfSetAsideDescription: Optional[str] = Field(None, description="Enter type Of SetAside Description.")
    typeOfSetAside: Optional[str] = Field(None, description="Enter type Of SetAside Code.")
    ncode: Optional[str] = Field(None, description="Enter Naics code.")
    ccode: Optional[str] = Field(None, description="Enter Classification code.")
    postedFrom: Optional[str] = Field(None, description="Enter posted from date in mm/dd/yyyy format. Required when providing limit.")
    postedTo: Optional[str] = Field(None, description="Enter posted to date in mm/dd/yyyy format. Required when providing limit.")
    rdlfrom: Optional[str] = Field(None, description="Enter response deadline in mm/dd/yyyy format")
    rdlto: Optional[str] = Field(None, description="Enter response deadline to in mm/dd/yyyy format")
    limit: Optional[int] = Field(None, description="Enter limit to fetch number of records")
    offset: Optional[int] = Field(None, description="Enter offset value")
    api_key: Optional[str] = Field(None, description="Enter the Public API Key.")

