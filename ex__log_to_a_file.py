import logging
import os

ROOT_DIR = "."
LOG_DIR = os.path.join(ROOT_DIR, "logs")
APP_DIR_LOG_PATH = os.path.join(LOG_DIR, "app.log")
DEBUG_DIR_LOG_PATH = os.path.join(LOG_DIR, "debug.log")

LOGGER_CONFIG = {
    "level": logging.DEBUG,
    "filename": APP_DIR_LOG_PATH,
    "filemode": "w",
    "format": "%(name)s - %(levelname)s - %(message)s",
}


def main():
    log_to_file()


def log_to_file():
    logging.basicConfig(**LOGGER_CONFIG)
    logging.debug("this will get get logged")
    logging.warning("this will get logged to a file")


if __name__ == "__main__":
    main()
