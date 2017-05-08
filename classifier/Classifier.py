import os.path
import sys
sys.path.append('../config')
sys.path.append('../log')
sys.path.append('../entities')
sys.path.append('../utils')
from config.Config import Config
from log.Logging import logging
from utils.NewFileUtils import NewFileUtils

class Classifier:

    def __init__(self, sourcePath, mediaType):
        self.numberOfErrors = 0
        self.sourcePath = sourcePath
        self.destinationPath = Config.get('classifier.path.destination')
        self.mediaType = mediaType

    def run(self):
        for filename in self.__getFilenamesToClassify():
            try:
                self.__classify(filename)
            except:
                self.__handleError(filename)
        NewFileUtils.removeDir(self.sourcePath)

    def __getFilenamesToClassify(self):
        extensions = tuple(Config.getFromSection(self.mediaType, 'classifier.path.sources.file.extensions').split(','))
        maxNumberOfFiles = int(Config.getFromSection(self.mediaType, 'classifier.max.number.of.files'))
        return NewFileUtils.findFilesRecursivelly(self.sourcePath, extensions, maxNumberOfFiles)

    def __classify(self, filename):
        NewFileUtils.move(filename, self.destinationPath)

    def __handleError(self, filename):
        self.numberOfErrors = self.numberOfErrors + 1
        logging.error('Error classifying %s. Error number %s.', str(filename), str(self.numberOfErrors), exc_info=True)
        if self.numberOfErrors == int(Config.get('classifier.max.number.of.errors')):
            raise ValueError('Too many errors. Something is wrong. Aborting execution.')
