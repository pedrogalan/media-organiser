from subprocess import Popen
from subprocess import PIPE
from MediaDate import MediaDate
from re import compile
import ntpath


class Media:

    def __init__(self, sourcePath):
        self.counter = 0
        self.sourcePath = sourcePath
        self.filename = self.__getFileName()
        self.fileext = self.__getFileExtension()
        self.createDate = self.__getDateFromMetaInfo()

    def getNextNewFileName(self):
        self.counter = self.counter + 1
        return self.getNewFileName(self.counter)

    def getNewFileName(self, counter):
        return self.createDate.toFileName() + "_" + str(counter).zfill(3) + "." + self.fileext

    def toString(self):
        return "Source path: " + self.sourcePath + \
               "\nCurrent filename: " + self.filename + \
               "\nProposed filename: " + self.getNextNewFileName()

    def __getDateFromMetaInfo(self):
        metainfo = self.__getMetaInformation()

        date = self.__getCreateDate(metainfo)
        if date is None:
            date = self.__getFileModificationDate(metainfo)

        return MediaDate(date)

    def __getMetaInformation(self):
        result = Popen(["exiftool", "-s", self.sourcePath], stdout=PIPE)
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
        return ntpath.basename(self.sourcePath)

    def __getFileExtension(self):
        return self.filename.split(".")[-1]
