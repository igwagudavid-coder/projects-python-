class WeatherServiceError(Exception):
    """Base exception for all weather service errors."""


class WeatherConnectionError(WeatherServiceError):
    """Raised when the application cannot connect to the weather service."""


class WeatherTimeoutError(WeatherServiceError):
    """Raised when the weather service takes too long to respond."""


class WeatherAPIError(WeatherServiceError):
    """Raised when the weather API returns an error response."""