import sys
sys.path.append('../utils')
from utils.MediaUtils import MediaUtils
from os.path import split
from DefaultFilenameParser import DefaultFilenameParser
from SamsungFilenameParser import SamsungFilenameParser
from Media import Media

class MediaBuilderFromFilename:

    def __init__(self, sourceFile):
        self.sourceFile = sourceFile

    def build(self):
        path, filename = split(self.sourceFile)
        fileext = self.__extractExtension(filename)
        mediaName = self.__parseFilename(filename)
        mediaType = MediaUtils.getMediaType(fileext)
        return Media(self.sourceFile, path, filename, fileext, mediaName, mediaType)

    def __extractExtension(self, filename):
        return filename.split('.')[-1].lower()

    def __parseFilename(self, filename):
        parsers = [SamsungFilenameParser, DefaultFilenameParser]
        for parser in parsers:
            try:
                return parser.parse(filename)
            except:
                pass
        raise ValueError('File name ' + filename + ' cannot be parsed.')
