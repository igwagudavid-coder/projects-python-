from app.api.weather_api import WeatherService
from app.exceptions.weather_exceptions import WeatherServiceError
from app.utils.logger import setup_logger
from config.settings import DEFAULT_CITY
from app.utils.formatters import WeatherFormatter

def main():
    logger = setup_logger()

    weather_service = WeatherService()

    try:

        weather = weather_service.get_current_weather(
            DEFAULT_CITY
        )

        logger.info("Weather downloaded successfully.")

        print(
            WeatherFormatter.format_for_console(
                weather
            )
        )

    except WeatherServiceError as error:
        logger.error(error)
        print(error)
        

if __name__ == "__main__":
    main()