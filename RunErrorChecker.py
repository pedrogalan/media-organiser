import logging
from error.ErrorChecker import ErrorChecker

try:
    ErrorChecker.check()
except:
    logging.error("Error checking the errors!", exc_info=True)
