from subprocess import Popen
from subprocess import PIPE
from MediaDate import MediaDate
from re import compile

class Media:

    def __init__(self, sourcePath):
        self.CREATE_DATE = compile("^CreateDate.*")
        self.sourcePath = sourcePath
        self.createDate = self.__getDateFromMetaInfo()

    def toString(self):
        return "Source path: " + self.sourcePath + "\nProposed filename: " + self.createDate.toFileName()

    def __getDateFromMetaInfo(self):
        return MediaDate(self.__getCreateDate())

    def __getCreateDate(self):
        metainf = self.__getMetaInformation().splitlines()
        for line in metainf:
            if self.CREATE_DATE.match(line):
                return line.split(": ")[-1];

    def __getMetaInformation(self):
        result = Popen(["exiftool", "-s", self.sourcePath], stdout=PIPE)
        return result.stdout.read()
