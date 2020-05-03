import logging
import os

ROOT_DIR = "."
LOG_DIR = os.path.join(ROOT_DIR, "logs")
APP_DIR_LOG_PATH = os.path.join(LOG_DIR, "app.log")


LOGGER_CONFIG = {
    "filename": APP_DIR_LOG_PATH,
    "filemode": "w",
}

LOGGER_CONFIG[
    "format"
] = "%(asctime)s | %(created)f | %(filename)s | %(funcName)s | %(levelname)s | %(message)s"

LOGGER_CONFIG["datefmt"] = "%Y-%m-%d %H:%M:%S %z"

logging.basicConfig(**LOGGER_CONFIG)

a = 5
b = 0

try:
    c = a / b

except ZeroDivisionError as e:
    logging.critical("exception!!!", exc_info=True)


# except ZeroDivisionError as e:
#     logging.error("exception!!!", exc_info=True)

# except ZeroDivisionError as e:
#     logging.exception("exception!!!")
