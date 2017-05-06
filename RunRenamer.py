#!/usr/bin/python

from log.Logging import logging
from renamer.Renamer import Renamer
from config.Config import Config
from utils import Locker

def __rename():
    for pathSource in Config.get('renamer.path.sources').split(','):
        try:
            Renamer(pathSource, 'Pictures').run()
            Renamer(pathSource, 'Videos').run()
        except ValueError as err:
            logging.error(str(err))

if Locker.startService('renamer'):
    __rename()
    Locker.stopService('renamer')
else:
    logging.error("The renamer could not start because there was a locker file.")
