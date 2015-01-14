from routing import status

class HereException(Exception):
    """Base exception for all pyhere-routing exceptions"""

class NoResults(HereException):
    """Raised when api returned no results"""

class RequestDenied(HereException):
    """Raised when request to API was denied"""

class InvalidRequest(HereException):
    """Raised when request to Google API was invalid"""
class RateLimitExceeded(HereException):
    """Raised when rate limit to API endpoint was exceeded"""

EXCEPTION_MAPPING = {
status.OK: None,
status.ZERO_RESULTS: NoResults,
status.REQUEST_DENIED: RequestDenied,
status.INVALID_REQUEST: InvalidRequest,
status.OVER_QUERY_LIMIT: RateLimitExceeded,
}
