#!/usr/bin/python

from log.Logging import logging
from classifier.Classifier import Classifier
from config.Config import Config

for pathSource in Config.get('classifier.path.sources').split(','):
    try:
        Classifier(pathSource, 'Pictures').run()
        Classifier(pathSource, 'Videos').run()
    except ValueError as err:
        logging.error(str(err))
