import logging
import os
from datetime import datetime

#create log folder if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

#file to store log 
log_file = "logs/automation.log"

#create logger object
logger = logging.getLogger("automation_logger")
logger.setLevel(logging.INFO)


#prevent duplicate logs
if logger.hasHandlers():
    logger.handlers.clear()

#formatter

form = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

#file handler
file = logging.FileHandler(log_file)
file.setFormatter(form)
logger.addHandler(file)

#console handler

console = logging.StreamHandler()
console.setFormatter(form)
logger.addHandler(console)






