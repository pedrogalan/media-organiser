import os.path
import sys
sys.path.append('../config')
sys.path.append('../utils')
from config.Config import Config
from utils.FileUtils import FileUtils
from utils.HandBrakeAdapter import HandBrakeAdapter

class VideoShrinker:

    def __init__(self, file, destinationPath):
        self.sourceFilename = file.fullPath
        self.destinationFilename = self.__buildDestinationFilename(file, destinationPath)

    def shrink(self):
        FileUtils.createDestinationDirectory(self.destinationFilename)
        HandBrakeAdapter.run(self.sourceFilename, self.destinationFilename)
        FileUtils.delete(self.sourceFilename)

    def __buildDestinationFilename(self, file, destinationPath):
        filePath = os.path.join(destinationPath, file.partialPath, file.name)
        filePathWithoutExtension = os.path.splitext(filePath)[0]
        newExtension = '.' + Config.get('handbrake.destination.extension')
        return filePathWithoutExtension + newExtension
