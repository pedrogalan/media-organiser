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

class Renamer:

    def __init__(self, sourcePath):
        self.numberOfErrors = 0
        self.sourcePath = sourcePath
        self.destinationPath = Config.get('renamer.path.destination')

    def run(self):
        for filename in self.__getFilenamesToRename():
            try:
                self.__rename(filename)
            except:
                self.__handleError(filename)

    def __getFilenamesToRename(self):
        extensions = tuple(Config.get('renamer.path.sources.file.extensions').split(','))
        return FileUtils.findFilesRecursivelly(self.sourcePath, extensions, Config.get('renamer.max.number.of.files'))

    def __rename(self, filename):
        media = Media(filename)
        FileUtils.rename(media, self.destinationPath)

    def __handleError(self, filename):
        self.numberOfErrors = self.numberOfErrors + 1
        logging.error("Error renaming %s. Error number %s.", filename, str(self.numberOfErrors), exc_info=True)
        if self.numberOfErrors == int(Config.get('renamer.max.number.of.errors')):
            raise ValueError('Too many errors. Something is wrong. Aborting execution.')
