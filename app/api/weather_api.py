import requests
from requests.exceptions import (
    HTTPError,
    ConnectionError,
    Timeout,
    RequestException,
)
from app.models.weather_data import WeatherData
from config.settings import(WEATHER_API_KEY, BASE_URL, REQUEST_TIMEOUT)


class WeatherService:
    def __init__(self):
        self.api_key = WEATHER_API_KEY
        self.base_url = BASE_URL
        self.timeout = REQUEST_TIMEOUT


    def build_url(self):
        return f"{self.base_url}/current.json"


    def build_parameters(self,city):
        return {
            "key": self.api_key,
            "q": city
        }
    def get_current_weather(self,city):
        url = self.build_url()
        parameters = self.build_parameters(city)
        response = self.send_request(url,parameters)
        return self.parse_response(response)


    def send_request(self,url , parameters):

        try:
            response = requests.get(url, params=parameters, timeout=self.timeout)
            response.raise_for_status()
            return response

        except Timeout:
            raise Exception("Connection request timed out")

        except ConnectionError:
            raise Exception("Unable to connect to server")

        except HTTPError as error:

            raise Exception(
                f"Weather API returned an error: {error}"
            )

        except RequestException as error:

            raise Exception(
                f"Unexpected request error: {error}"
            )

    def parse_response(self,response):
        data = response.json()
        location = data["location"]
        current = data["current"]
        return WeatherData(
            city=location["name"],
            country=location["country"],
            temperature=current["temp_c"],
            humidity=current["humidity"],
            wind_speed=current["wind_kph"],
            condition=current["condition"]["text"]
        )