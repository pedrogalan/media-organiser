#!/usr/bin/python

from log.Logging import logging
from classifier.Classifier import Classifier
from config.Config import Config
from utils import Locker

def __classify():
    for pathSource in Config.get('classifier.path.sources').split(','):
        try:
            Classifier(pathSource, 'Pictures').run()
            Classifier(pathSource, 'Videos').run()
        except Exception as err:
            logging.error(str(err))

if Locker.startService():
    logging.warning("Starting the classifier...")
    __classify()
    Locker.stopService()
else:
    logging.error("The classifier could not start because there was a locker file.")
