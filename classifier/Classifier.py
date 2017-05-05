import os.path
import sys
sys.path.append('../config')
sys.path.append('../log')
sys.path.append('../entities')
sys.path.append('../utils')
from config.Config import Config
from log.Logging import logging
from entities.File import File
from utils.FileUtils import FileUtils
from glob import glob

class Classifier:

    def __init__(self, sourcePath):
        self.numberOfErrors = 0
        self.sourcePath = sourcePath
        self.destinationPath = Config.get('classifier.path.destination')

    def run(self):
        for filename in self.__getFilenamesToClassify():
            try:
                self.__classify(filename)
            except:
                self.__handleError(filename)

    def __getFilenamesToClassify(self):
        extensions = tuple(Config.get('classifier.path.sources.file.extensions').split(','))
        return FileUtils.findFilesRecursivelly(self.sourcePath, extensions, Config.get('classifier.max.number.of.files'))

    def __classify(self, filename):
        file = File(filename)
        destinationFilename = self.__buildDestinationFilename(file, self.destinationPath)
        FileUtils.move(file.fullPath, destinationFilename)

    def __buildDestinationFilename(self, file, destinationPath):
        return os.path.join(destinationPath, file.partialPath, file.name)

    def __handleError(self, filename):
        self.numberOfErrors = self.numberOfErrors + 1
        logging.error('Error classifying %s. Error number %s.', str(filename), str(self.numberOfErrors), exc_info=True)
        if self.numberOfErrors == int(Config.get('classifier.max.number.of.errors')):
            raise ValueError('Too many errors. Something is wrong. Aborting execution.')
