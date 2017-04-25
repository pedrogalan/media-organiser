from subprocess import Popen
from subprocess import PIPE
from MediaDate import MediaDate
from re import compile

class Media:

    def __init__(self, sourcePath):
        self.sourcePath = sourcePath
        self.createDate = self.__getDateFromMetaInfo()

    def toString(self):
        return "Source path: " + self.sourcePath + "\nProposed filename: " + self.createDate.toFileName()

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
        print metainfo
        return self.__getDate(metainfo, compile("^FileModifyDate.*"))

    def __getDate(self, metainfo, fieldname):
        for line in metainfo.splitlines():
            if fieldname.match(line):
                return line.split(": ")[-1];
