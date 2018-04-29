#!/usr/bin/python

from log.Logging import logging
from normaliser.Normaliser import Normaliser
from config.Config import Config
from utils import Locker

def __normalise():
    for pathSource in Config.get('normaliser.path.sources').split(','):
        try:
            Normaliser(pathSource, 'Pictures').run()
            # Normaliser(pathSource, 'Videos').run()
        except Exception as err:
            logging.error(str(err))

if Locker.startService():
    __normalise()
    Locker.stopService()
else:
    logging.error("The normaliser could not start because there was a locker file.")
