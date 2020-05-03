import logging
import logging.config

file_config_kwargs = {
    "fname": "file.conf",
    "disable_existing_loggers": False,
}

logging.config.fileConfig(**file_config_kwargs)


# Get the logger specified in the file
logger = logging.getLogger(__name__)
logger.debug(f"This is a debug message from {__file__}")
