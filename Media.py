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
        self.type = self.__extractMimeTypeFromMetaInfo()

    def getNextNewFileName(self):
        self.counter = self.counter + 1
        return self.getNewFileName(self.counter)

    def getNewFileName(self, counter):
        return self.createDate.toFileName() + "_" + str(counter).zfill(3) + self.__getFileExtension()

    def __extractMimeTypeFromMetaInfo(self):
        print self.__getDate(self.metainfo, compile("^MIMEType.*"))

    def __getDateFromMetaInfo(self):
        date = self.__getCreateDate(self.metainfo)
        if date is None:
            date = self.__getFileModificationDate(self.metainfo)

        return MediaDate(date)

    def __getMetaInformation(self):
        result = Popen(["exiftool", "-s", self.sourceFile], stdout=PIPE)
        return result.stdout.read()

    def __getCreateDate(self, metainfo):
        return self.__getDate(metainfo, compile("^CreateDate.*"))

    def __getFileModificationDate(self, metainfo):
        return self.__getDate(metainfo, compile("^FileModifyDate.*"))

    def __getDate(self, metainfo, fieldname):
        for line in metainfo.splitlines():
            if fieldname.match(line):
                return line.split(": ")[-1];

    def __getFileName(self):
        return ntpath.basename(self.sourceFile)

    def __extractFileExtension(self):
        if "." in self.filename:
            return self.filename.split(".")[-1]
        else:
            return ""

    def __getFileExtension(self):
        if "" is self.fileext:
            return self.fileext
        else:
            return "." + self.fileext
