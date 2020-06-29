import logging
from os import remove , path


log_file = "/tmp/robocar_error.log"

my_formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
f_handler = logging.FileHandler(log_file)
f_handler.setLevel(logging.WARNING)

# Create formatters and add it to handlers
f_format = logging.Formatter(my_formatter)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(f_handler)

def log_warning(message):
    print(message)
    logger.warning(message)

def log_critical(message):
    print(message)
    logger.critical(message)

def log_error(message):
    print(message)
    logger.error(message)

def clear_logs():
    if path.exists(log_file):
        remove(log_file)
    else:
        pass
