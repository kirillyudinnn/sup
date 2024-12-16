class KinopoiskApiError(Exception):
    """Base exception for Kinopoisk API errors."""
    pass

class UnauthorizedError(KinopoiskApiError):
    """Exception for 401 Unauthorized errors."""
    pass

class ForbiddenError(KinopoiskApiError):
    """Exception for 403 Forbidden errors."""
    pass
