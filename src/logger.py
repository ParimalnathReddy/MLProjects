import logging
import os
from datetime import datetime

# Define the log file name using strftime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory where logs will be stored
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Define the full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure the logging module to write logs to the specified file
logging.basicConfig(filename=LOG_FILE_PATH, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    level=logging.INFO)


if __name__ == "__main__":
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")