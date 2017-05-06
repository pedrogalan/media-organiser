#!/usr/bin/python

from log.Logging import logging
from renamer.Renamer import Renamer
from config.Config import Config

for pathSource in Config.get('renamer.path.sources').split(','):
    try:
        Renamer(pathSource, 'Pictures').run()
        Renamer(pathSource, 'Videos').run()
    except ValueError as err:
        logging.error(str(err))
