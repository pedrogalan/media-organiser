from subprocess import Popen
from subprocess import PIPE
from MediaDate import MediaDate
from re import compile
import ntpath


class Media:

    def __init__(self, sourceFile):
        self.counter = 0
        self.sourceFile = sourceFile
        self.metainfo = self.__getMetaInformation()
        self.filename = self.__getFileName()
        self.fileext = self.__extractFileExtension()
        self.createDate = self.__getDateFromMetaInfo()
        self.createYear = self.__extractCreateYear()
        self.type = self.__extractMimeTypeFromMetaInfo()

    def getNextNewFileName(self):
        self.counter = self.counter + 1
        return self.getNewFileName(self.counter)

    def getNewFileName(self, counter):
        return self.createDate.toFileName() + "_" + str(counter).zfill(3) + self.fileext

    def isPicture(self):
        return self.type == "image"

    def isVideo(self):
        return self.type == "video"

    def getCreateYear(self):
        return self.createYear

    def __extractMimeTypeFromMetaInfo(self):
        mimeType = self.__getMetainfoValue(self.metainfo, compile("^MIMEType.*"))
        if mimeType is None:
            return "unknown"
        else:
            return mimeType.split("/")[0]

    def __getDateFromMetaInfo(self):
        date = self.__getCreateDate(self.metainfo)
        if date is None:
            date = self.__getFileModificationDate(self.metainfo)

        return MediaDate(date)

    def __getMetaInformation(self):
        result = Popen(["exiftool", "-s", self.sourceFile], stdout=PIPE)
        return result.stdout.read()

    def __getCreateDate(self, metainfo):
        return self.__getMetainfoValue(metainfo, compile("^CreateDate.*"))

    def __getFileModificationDate(self, metainfo):
        return self.__getMetainfoValue(metainfo, compile("^FileModifyDate.*"))

    def __getMetainfoValue(self, metainfo, fieldname):
        for line in metainfo.splitlines():
            if fieldname.match(line):
                return line.split(": ")[-1];

    def __getFileName(self):
        return ntpath.basename(self.sourceFile)

    def __extractFileExtension(self):
        # TODO Extract the extension from the metainfo
        if "." in self.filename:
            return self.filename.split(".")[-1].lower()
        else:
            return ""

    def __extractCreateYear(self):
        return self.createDate.getYear()
