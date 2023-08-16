
import pytest
from opportunities_api.utils import parse_date, format_date, handle_pagination
from datetime import datetime

def test_date_parsing_and_formatting():
    date_str = "2021-01-01"
    date_obj = datetime(2021, 1, 1)
    assert parse_date(date_str) == date_obj
    assert format_date(date_obj) == date_str

def test_handle_pagination():
    pagination = handle_pagination(page=2, size=10)
    assert pagination["page"] == 2
    assert pagination["size"] == 10
