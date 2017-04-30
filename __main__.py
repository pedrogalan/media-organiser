#!/usr/bin/python

from renamer.Renamer import Renamer
from config.Config import Config
import logging

logging.basicConfig(filename=Config.get('log.file.location'),          \
                    format='[%(asctime)s][%(levelname)s] %(message)s', \
                    datefmt='%d/%m/%Y %H:%M:%S')

for pathSource in Config.get('path.sources').split(','):
    try:
        Renamer(pathSource).run()
    except ValueError as err:
        logging.error(str(err))
