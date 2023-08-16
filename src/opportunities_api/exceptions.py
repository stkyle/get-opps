
class OpportunitiesAPIException(Exception):
    """Base exception class for Opportunities API errors."""
    pass

class RateLimitExceededException(OpportunitiesAPIException):
    """Exception raised when rate limit is exceeded."""
    pass

class UnauthorizedAccessException(OpportunitiesAPIException):
    """Exception raised when unauthorized access is attempted."""
    pass

class GeneralAPIException(OpportunitiesAPIException):
    """Exception raised for general API errors."""
    pass
