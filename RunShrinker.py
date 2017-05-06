#!/usr/bin/python

from log.Logging import logging
from shrinker.Shrinker import Shrinker
from config.Config import Config

for pathSource in Config.get('shrinker.path.sources').split(','):
    try:
        Shrinker(pathSource, 'Pictures').run()
        Shrinker(pathSource, 'Videos').run()
    except ValueError as err:
        logging.error(str(err))
