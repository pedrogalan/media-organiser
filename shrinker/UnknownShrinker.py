import os.path

class UnknownShrinker:

    def __init__(self, file, destinationPath):
        self.sourceFilename = file.fullPath
        self.destinationFilename = self.__buildDestinationFilename(file, destinationPath)

    def shrink(self):
        FileUtils.move(self.sourceFilename, self.destinationFilename)

    def __buildDestinationFilename(self, file, destinationPath):
        return os.path.join(destinationPath, file.partialPath, file.name)
