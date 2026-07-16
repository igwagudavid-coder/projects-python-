from pathlib import Path
import os


from dotenv  import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "https://api.weatherapi.com/v1"

REQUEST_TIMEOUT = 30

DEFAULT_CITY = "Abuja, NG"
