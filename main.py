from app.utils.logger import logger
from config.settings import DEFAULT_CITY


def main():
    logger.info("Weather prediction system has started!")
    logger.info(f"Default city is : {DEFAULT_CITY}")



if __name__ == "__main__":
    main()