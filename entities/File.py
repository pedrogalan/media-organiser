import os.path

class File:

    def __init__(self, filename):
        self.name = os.path.basename(filename)
        self.fullPath = os.path.dirname(filename)
        self.partialPath = self.__extractPartialPath()

    def __extractPartialPath(self):
        head, year = os.path.split(self.fullPath)
        head, mediaType = os.path.split(head)
        return os.path.join(mediaType, year)
