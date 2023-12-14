import logging
from logging.handlers import RotatingFileHandler

# Configure the root logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Create a FileHandler and add it to the root logger
file_handler = RotatingFileHandler("app.log", maxBytes=1e6, backupCount=3)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logging.getLogger().addHandler(file_handler)