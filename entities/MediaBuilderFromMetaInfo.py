import sys
sys.path.append('../utils')
from utils.MediaUtils import MediaUtils
from re import compile
from os.path import split
from subprocess import Popen
from subprocess import PIPE
from NewMedia import NewMedia
from MediaDate import MediaDate
from MediaName import MediaName

class MediaBuilderFromMetaInfo:

    def __init__(self, sourceFile):
        self.sourceFile = sourceFile
        self.metainfo = self.__getMetaInformation()

    def build(self):
        path, filename = split(self.sourceFile)
        fileext = self.__getExtension()
        mediaName = self.__getMediaNameFromMetaInfo()
        mediaType = self.__getMimeTypeFromMetaInfo()
        return NewMedia(self.sourceFile, path, filename, fileext, mediaName, mediaType)

    def __getMetaInformation(self):
        result = Popen(['exiftool', '-s', self.sourceFile], stdout=PIPE)
        return result.stdout.read()

    def __getMimeTypeFromMetaInfo(self):
        mimeType = self.__getMetaInfoValue(compile('^MIMEType.*'))
        if mimeType is None:
            return MediaUtils.getMediaType(self.__getExtension())
        else:
            return mimeType.split('/')[0]

    def __getMediaNameFromMetaInfo(self):
        mediaDate = self.__getDateFromMetaInfo()
        return MediaName(mediaDate, 1)

    def __getDateFromMetaInfo(self):
        date = self.__getCreateDateFromMetaInfo()
        if date is None or date == '0000:00:00 00:00:00':
            date = self.__getFileModificationDateFromMetaInfo()
        return MediaDate(date)

    def __getCreateDateFromMetaInfo(self):
        return self.__getMetaInfoValue(compile('^CreateDate.*'))

    def __getFileModificationDateFromMetaInfo(self):
        return self.__getMetaInfoValue(compile('^FileModifyDate.*'))

    def __getExtensionFromMetaInfo(self):
        return self.__getMetaInfoValue(compile('^FileTypeExtension.*'))

    def __getMetaInfoValue(self, fieldname):
        for line in self.metainfo.splitlines():
            if fieldname.match(line):
                return line.split(': ')[-1];

    def __getExtension(self):
        fileext = self.__getExtensionFromMetaInfo()
        if fileext is None:
            fileext = self.sourceFile.split('.')[-1].lower()
        return fileext
