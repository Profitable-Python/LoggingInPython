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

LOGGER_CONFIG[
    "format"
] = "%(asctime)s | %(created)f | %(filename)s | %(funcName)s | %(levelname)s | %(message)s"

LOGGER_CONFIG["datefmt"] = "%d-%b-%y %H:%M:%S"
LOGGER_CONFIG["datefmt"] = "%Y-%m-%d %H:%M:%S %z"


def main():
    configure_logger()
    log_warning()
    log_debug()
    log_warning()


def configure_logger():
    logging.basicConfig(**LOGGER_CONFIG)


def log_debug():
    logging.debug("this will get get logged")


def log_warning():
    logging.warning("this will get logged to a file")


if __name__ == "__main__":
    main()
