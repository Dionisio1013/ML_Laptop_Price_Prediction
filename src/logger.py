# any execution should be able to be logged/tracked even in the custom exception error
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(), "logs", LOG_FILE)
# Even though there is a file keep on appending the continous changes
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Whenever you use logging.info it will create the file path with the format 
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO

)

if __name__ == "__main__":
    logging.info("Logging has started")