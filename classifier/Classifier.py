import sys
sys.path.append('../config')
sys.path.append('../log')
sys.path.append('../entities')
sys.path.append('../utils')
from config.Config import Config
from log.Logging import logging
from entities.Media import Media
from utils.FileUtils import FileUtils
from glob import glob

class Classifier:

    def __init__(self, sourcePath):
        self.numberOfErrors = 0
        self.sourcePath = sourcePath
        self.destinationPath = Config.get('classifier.path.destination')

    def run(self):
        print 'Running classifier.'
