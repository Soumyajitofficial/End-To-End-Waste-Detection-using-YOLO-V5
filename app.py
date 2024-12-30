from wasteDetection.logger import logging
import sys

logging.info("Welcome to the waste detection system")

from wasteDetection.exception import Waste_Exception

try:
    a = 7/0

except Exception as e:
    raise Waste_Exception(e,sys) from e
