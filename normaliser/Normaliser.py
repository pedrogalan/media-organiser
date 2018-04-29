import sys
sys.path.append('../config')
sys.path.append('../log')
sys.path.append('../entities')
sys.path.append('../utils')
from entities.MediaBuilder import MediaBuilder
from config.Config import Config
from log.Logging import logging
from utils.FileUtils import FileUtils
from glob import glob
from entities.MediaBuilderFromMetaInfo import MediaBuilderFromMetaInfo
from subprocess import Popen
from subprocess import PIPE

class Normaliser:

    def __init__(self, sourcePath, mediaType):
        self.numberOfErrors = 0
        self.sourcePath = sourcePath
        self.destinationPath = Config.get('normaliser.path.destination')
        self.mediaType = mediaType

    def run(self):
        for filename in self.__getFilenamesToNormalise():
            try:
                self.__normalise(filename)
            except:
                self.__handleError(filename)

    def __getFilenamesToNormalise(self):
        extensions = tuple(Config.getFromSection(self.mediaType, 'normaliser.path.sources.file.extensions').split(','))
        maxNumberOfFiles = int(Config.getFromSection(self.mediaType, 'normaliser.max.number.of.files'))
        return FileUtils.findFilesRecursivelly(self.sourcePath, extensions, maxNumberOfFiles)

    def __normalise(self, sourceFilename):
        media = MediaBuilder.build(sourceFilename)

        if media.getCreationDate().getOrigin() != "DateTimeOriginal":
            self.__setDateTimeOriginal(media)

        FileUtils.mv(sourceFilename, self.destinationPath + '/')

    def __setDateTimeOriginal(self, media):
        creationDate = media.getCreationDate()
        filename = media.getFullPath()
        Popen(['exiftool', '-overwrite_original', '-datetimeoriginal=' + str(creationDate), filename], stdout=PIPE)

    def __handleError(self, filename):
        self.numberOfErrors = self.numberOfErrors + 1
        logging.error("Error normalising %s. Error number %s.", filename, str(self.numberOfErrors), exc_info=True)
        if self.numberOfErrors == int(Config.get('normaliser.max.number.of.errors')):
            raise ValueError('Too many errors. Something is wrong. Aborting execution.')
