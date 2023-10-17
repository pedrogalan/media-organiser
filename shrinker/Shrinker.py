import sys
sys.path.append('../config')
sys.path.append('../log')
sys.path.append('../entities')
sys.path.append('../utils')
from config.Config import Config
from log.Logging import logging
from entities.Media import Media
from entities.MediaBuilder import MediaBuilder
from utils.FileUtils import FileUtils
from . VideoShrinker import VideoShrinker
from . PictureShrinker import PictureShrinker
from . UnknownShrinker import UnknownShrinker
from glob import glob

class Shrinker:

    def __init__(self, sourcePath, mediaType):
        self.numberOfErrors = 0
        self.sourcePath = sourcePath
        self.destinationPath = Config.get('shrinker.path.destination')
        self.mediaType = mediaType

    def run(self):
        for filename in self.__getFilenamesToShrink():
            try:
                self.__shrink(filename)
            except:
                self.__handleError(filename)
        FileUtils.removeDir(self.sourcePath)

    def __getFilenamesToShrink(self):
        extensions = tuple(Config.getFromSection(self.mediaType, 'shrinker.path.sources.file.extensions').split(','))
        maxNumberOfFiles = int(Config.getFromSection(self.mediaType, 'shrinker.max.number.of.files'))
        return FileUtils.findFilesRecursivelly(self.sourcePath, extensions, maxNumberOfFiles)

    def __shrink(self, filename):
        media = MediaBuilder.build(filename)
        if media.isVideo():
            VideoShrinker(filename, self.destinationPath).shrink()
        elif media.isPicture():
            PictureShrinker(filename, self.destinationPath).shrink()
        else:
            UnknownShrinker(filename, self.destinationPath).shrink()

    def __handleError(self, filename):
        self.numberOfErrors = self.numberOfErrors + 1
        logging.error('Error shrinking %s. Error number %s.', str(filename), str(self.numberOfErrors), exc_info=True)
        if self.numberOfErrors == int(Config.get('shrinker.max.number.of.errors')):
            raise ValueError('Too many errors. Something is wrong. Aborting execution.')
