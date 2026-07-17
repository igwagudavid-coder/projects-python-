from app.models.weather_data import WeatherData
class WeatherFormatter:


    @staticmethod
    def format_for_console(weather:WeatherData) -> str:
        return (
            f"City: {weather.city}\n"
            f"Country: {weather.country}\n"
            f"Temperature: {weather.temperature}°C\n"
            f"Humidity: {weather.humidity}%\n"
            f"Wind Speed: {weather.wind_speed} km/h\n"
            f"Condition: {weather.condition}"
        )
