import os.path

class File:

    def __init__(self, filename):
        self.fullPath = filename
        self.name = os.path.basename(filename)
        self.path = os.path.dirname(filename)
        self.partialPath = self.__extractPartialPath()

    def __extractPartialPath(self):
        head, year = os.path.split(self.path)
        head, mediaType = os.path.split(head)
        return os.path.join(mediaType, year)
