import sys
sys.path.append('../utils')
from utils.FileUtils import FileUtils

class PictureShrinker:

    def __init__(self, filename, destinationPath):
        self.sourceFilename = filename
        self.destinationPath = destinationPath

    def shrink(self):
        FileUtils.move(self.sourceFilename, self.destinationPath)
