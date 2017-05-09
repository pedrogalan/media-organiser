import sys
sys.path.append('../config')
sys.path.append('../log')
sys.path.append('../entities')
sys.path.append('../utils')
from config.Config import Config
from log.Logging import logging
from utils.FileUtils import FileUtils
from glob import glob

class Renamer:

    def __init__(self, sourcePath, mediaType):
        self.numberOfErrors = 0
        self.sourcePath = sourcePath
        self.destinationPath = Config.get('renamer.path.destination')
        self.mediaType = mediaType

    def run(self):
        for filename in self.__getFilenamesToRename():
            try:
                self.__rename(filename)
            except:
                self.__handleError(filename)

    def __getFilenamesToRename(self):
        extensions = tuple(Config.getFromSection(self.mediaType, 'renamer.path.sources.file.extensions').split(','))
        maxNumberOfFiles = int(Config.getFromSection(self.mediaType, 'renamer.max.number.of.files'))
        return FileUtils.findFilesRecursivelly(self.sourcePath, extensions, maxNumberOfFiles)

    def __rename(self, filename):
        FileUtils.move(filename, self.destinationPath)

    def __handleError(self, filename):
        self.numberOfErrors = self.numberOfErrors + 1
        logging.error("Error renaming %s. Error number %s.", filename, str(self.numberOfErrors), exc_info=True)
        if self.numberOfErrors == int(Config.get('renamer.max.number.of.errors')):
            raise ValueError('Too many errors. Something is wrong. Aborting execution.')
