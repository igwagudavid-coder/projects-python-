import logging
from pathlib import Path
from config.settings import BASE_DIR
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok= True)
LOG_FILE = LOG_DIR / "weather prediction.log"
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s",
    handlers = [
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]

)
logger = logging.getLogger(__name__)
