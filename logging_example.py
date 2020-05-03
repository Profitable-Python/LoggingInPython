import logging
import os

ROOT_DIR = "."
LOG_DIR = os.path.join(ROOT_DIR, "logs")
LOG_FILE_PATH = os.path.join(LOG_DIR, "file.log")

"""
DEBUG
INFO
## DEFAULTS BELOW
WARNING
ERROR
CRITICAL
"""

# create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(LOG_FILE_PATH)
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters
## is there a pylint extension for python logger
# c_format = logging.Formatter(f"{name} - {levelname} - {message}")
# f_format = logging.Formatter(f"{asctime} - {name} - {levelname} - {message}")

c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning("Warning !@^#$^%#$@#")
logger.error("ERRORORORORORORSSSZZZ")
