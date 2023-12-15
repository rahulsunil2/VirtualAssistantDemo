import logging
import sys


logger = logging.getLogger()
logger.setLevel(logging.WARNING)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
