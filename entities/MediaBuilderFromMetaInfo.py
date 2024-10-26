import sys
sys.path.append('../utils')
from utils.MediaUtils import MediaUtils
from re import compile
from os.path import split
from subprocess import Popen
from subprocess import PIPE
from . Media import Media
from . MediaDate import MediaDate
from . MediaName import MediaName

class MediaBuilderFromMetaInfo:

    def __init__(self, sourceFile):
        self.sourceFile = sourceFile
        self.metainfo = self.__getMetaInformation()

    def build(self):
        fileext = self.__getExtension()
        mediaName = self.__getMediaNameFromMetaInfo()
        mediaType = self.__getMimeTypeFromMetaInfo()
        mediaDate = self.__getDateFromMetaInfo()
        return Media('METADATA', self.sourceFile, fileext, mediaName, mediaType, mediaDate)

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
        return MediaName(mediaDate)

    def __getDateFromMetaInfo(self):
        date = self.__getDateTimeOriginalFromMetaInfo()
        origin = "DateTimeOriginal"
        if date is None or date == '0000:00:00 00:00:00':
            date = self.__getCreateDateFromMetaInfo()
            origin = "CreateDate"
            if date is None or date == '0000:00:00 00:00:00':
                date = self.__getFileModificationDateFromMetaInfo()
                origin = "FileModifyDate"
        return MediaDate(date, origin)

    def __getCreateDateFromMetaInfo(self):
        return self.__getMetaInfoValue(compile('^CreateDate.*'))

    def __getDateTimeOriginalFromMetaInfo(self):
        return self.__getMetaInfoValue(compile('^DateTimeOriginal.*'))

    def __getFileModificationDateFromMetaInfo(self):
        return self.__getMetaInfoValue(compile('^FileModifyDate.*'))

    def __getExtensionFromMetaInfo(self):
        return self.__getMetaInfoValue(compile('^FileTypeExtension.*'))

    def __getMetaInfoValue(self, fieldname):
        for line in self.metainfo.splitlines():
            if fieldname.match(line.decode('utf-8')):
                return line.decode('utf-8').split(': ')[-1];

    def __getExtension(self):
        fileext = self.__getExtensionFromMetaInfo()
        if fileext is None:
            fileext = self.sourceFile.split('.')[-1].lower()
        return fileext
