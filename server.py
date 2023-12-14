import os
from uvicorn import run
from app import app
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)



if __name__ == "__main__":
    run(app,  log_level="info" , log_config=logging.basicConfig())