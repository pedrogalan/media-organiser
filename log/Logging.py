import logging
import sys
sys.path.append('../config')
from config.Config import Config

logging.basicConfig(filename=Config.get('log.file.location'),          \
                    format='[%(asctime)s][%(levelname)s] %(message)s', \
                    datefmt='%d/%m/%Y %H:%M:%S')
