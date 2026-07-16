import logging
from config.settings import BASE_DIR

LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "weather_prediction.log"

def setup_logger():
    logger = logging.getLogger("weather_prediction")
    if logger.handlers:
        return logger

    LOG_DIR.mkdir(exist_ok =True)
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s | %(levelname)s | %(message)s",
        handlers = [
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("weather_prediction")
