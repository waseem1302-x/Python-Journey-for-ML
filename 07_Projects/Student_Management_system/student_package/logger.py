import logging
import os
from datetime import datetime

# ============================
# Logger Setup for SMS Package
# ============================

LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, f"sms.log")

# Configure logger
logger = logging.getLogger("SMS_Logger")
logger.setLevel(logging.DEBUG)  # Capture everything: DEBUG, INFO, WARNING, ERROR, CRITICAL

# File Handler (saves logs to file)
file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Log format
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)

# Avoid duplicate handlers if re-imported
if not logger.hasHandlers():
    logger.addHandler(file_handler)
