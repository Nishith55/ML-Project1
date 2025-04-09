# import logging
# import os
# from datetime import datetime

# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(logs_path,exist_ok=True)

# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,


# )

# if __name__  == "_main_":
#     logging.info("Logging has started")
#     print("Logger is working. Check the logs folder.")

# import logging
# import os
# from datetime import datetime

# # Set up log directory and filename
# logs_dir = os.path.join(os.getcwd(), "logs")
# os.makedirs(logs_dir, exist_ok=True)

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# # Configure logging
# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

# if __name__ == "__main__":
#     logging.info("Logging has started")
#     print("Logging is set up. Check logs folder.")


import logging
import os
from datetime import datetime

# Create a nested logs/log/ directory
logs_dir = os.path.join(os.getcwd(), "logs", "log")
os.makedirs(logs_dir, exist_ok=True)

# Generate the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()  # This will also print to terminal
    ]
)

if __name__ == "__main__":
    logging.info("Logging has started")
    print(f"Log file created at: {LOG_FILE_PATH}")
