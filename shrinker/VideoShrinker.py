import os.path

class VideoShrinker:

    def __init__(self, file, destinationPath):
        self.sourceFilename = file.fullPath
        self.destinationFilename = self.__buildDestinationFilename(file, destinationPath)

    def shrink(self):
        print('Shrinking video:\nFrom: ' + self.sourceFilename + '\nTo  : ' + self.destinationFilename)

    def __buildDestinationFilename(self, file, destinationPath):
        return os.path.join(destinationPath, file.partialPath, file.name)
