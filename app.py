from SignLanguage.logger import logging
from SignLanguage.exception import SignException
logging.info("Welcome to the Project.")
import sys

try: 
    a = 7/0
except Exception as e:
    raise SignException(e, sys) from e
