import sys
sys.path.append('../utils')
from utils.NewFileUtils import NewFileUtils

class PictureShrinker:

    def __init__(self, filename, destinationPath):
        self.sourceFilename = filename
        self.destinationPath = destinationPath

    def shrink(self):
        NewFileUtils.move(self.sourceFilename, self.destinationPath)
