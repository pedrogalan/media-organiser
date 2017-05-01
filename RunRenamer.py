#!/usr/bin/python

from log.Logging import logging
from renamer.Renamer import Renamer
from config.Config import Config

for pathSource in Config.get('path.sources').split(','):
    try:
        Renamer(pathSource).run()
    except ValueError as err:
        logging.error(str(err))
