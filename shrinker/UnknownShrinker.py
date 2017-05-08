import sys
sys.path.append('../log')
from log.Logging import logging

class UnknownShrinker:

    def __init__(self, filename, destinationPath):
        self.sourceFilename = filename
        self.destinationPath = destinationPath

    def shrink(self):
        logging.error('File %s cannot be shrinked because its type is unknown.', self.sourceFilename)
