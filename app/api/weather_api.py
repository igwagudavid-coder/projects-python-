import requests
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
        response = requests.get(url, params=parameters, timeout=self.timeout)
        response.raise_for_status()
        return response

    def parse_response(self,response):
        return response.json()