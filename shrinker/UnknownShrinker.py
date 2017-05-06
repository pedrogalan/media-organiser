import os.path
import sys
sys.path.append('../log')
from log.Logging import logging

class UnknownShrinker:

    def __init__(self, file, destinationPath):
        self.sourceFilename = file.fullPath
        self.destinationFilename = self.__buildDestinationFilename(file, destinationPath)

    def shrink(self):
        logging.error('File %s cannot be shrinked because its type is unknown.', self.sourceFilename)

    def __buildDestinationFilename(self, file, destinationPath):
        return os.path.join(destinationPath, file.partialPath, file.name)
