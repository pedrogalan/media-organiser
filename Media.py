from subprocess import call
class Media:

    def __init__(self, sourcePath):
        self.sourcePath = sourcePath

    def getCreationDate(self):
        return "the-creation-date"

    def getMetaInformation(self):
        call(["exiftool", self.sourcePath])
