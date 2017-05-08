#!/usr/bin/python

from log.Logging import logging
from shrinker.Shrinker import Shrinker
from config.Config import Config
from utils import Locker


def __shrink():
    for pathSource in Config.get('shrinker.path.sources').split(','):
        try:
            Shrinker(pathSource, 'Pictures').run()
            Shrinker(pathSource, 'Videos').run()
        except Exception as err:
            logging.error(str(err))

if Locker.startService():
    __shrink()
    Locker.stopService()
else:
    logging.error("The shrinker could not start because there was a locker file.")
