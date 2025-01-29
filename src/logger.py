# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import os
import logging
from dotenv import load_dotenv

# Enable initial logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

load_dotenv()
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Check if the LOG_LEVEL is correct
if LOG_LEVEL.lower() not in ["debug", "info", "warning", "error", "critical"]:
    logger.warning("LOG_LEVEL is not correct. Defaulting to INFO")
    LOG_LEVEL = "INFO"
else:
    # Use lazy % formatting in logging functions (PylintW1203:logging-fstring-interpolation)
    logger.info("Setting log level to %s", LOG_LEVEL.upper())

# Set the user-defined log level
logger.setLevel(LOG_LEVEL.upper())

# Export the logger instance directly
debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
critical = logger.critical
