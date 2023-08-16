
from datetime import datetime

# Constants
DATE_FORMAT = "%Y-%m-%d"

# Utility Functions

def parse_date(date_str: str) -> datetime:
    """Parses a date string into a datetime object."""
    return datetime.strptime(date_str, DATE_FORMAT)

def format_date(date: datetime) -> str:
    """Formats a datetime object into a string."""
    return date.strftime(DATE_FORMAT)

def handle_pagination(page: int, size: int) -> dict:
    """Returns pagination parameters for API requests."""
    return {"page": page, "size": size}
