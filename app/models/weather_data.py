from dataclasses import dataclass
@dataclass
class WeatherData:
    city: str
    country: str
    temperature :float
    humidity : int
    wind_speed :float
    condition :str