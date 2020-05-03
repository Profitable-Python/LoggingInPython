
import logging
import logging.config
import os 
from pprint import pprint
import yaml


ROOT = os.path.dirname(os.path.abspath(__file__))
YAML_FILE_PATH = os.path.join(ROOT, 'config.yml')
YML_EXISTS = os.path.exists(YAML_FILE_PATH)
print(f"my yaml exists right?: {YML_EXISTS}")

with open(YAML_FILE_PATH, "r") as fin:

    config = yaml.safe_load(fin)
    # pprint(config)
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
logger.debug("This is a debug message")
