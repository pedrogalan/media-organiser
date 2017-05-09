import os.path
import sys
sys.path.append('../config')
sys.path.append('../utils')
sys.path.append('../entities')
from config.Config import Config
from utils.FileUtils import FileUtils
from entities.MediaBuilder import MediaBuilder
from utils.HandBrakeAdapter import HandBrakeAdapter

class VideoShrinker:

    def __init__(self, filename, destinationPath):
        self.sourceFilename = filename
        self.destinationFilename = self.__buildDestinationFilename(filename, destinationPath)

    def shrink(self):
        FileUtils.createDestinationDirectory(self.destinationFilename)
        HandBrakeAdapter.run(self.sourceFilename, self.destinationFilename)
        FileUtils.delete(self.sourceFilename)

    def __buildDestinationFilename(self, filename, destinationPath):
        media = MediaBuilder.build(filename)
        partialPath = FileUtils.getDestinationSubdirectory(media)
        filePath = os.path.join(destinationPath, partialPath, media.getNextNewFileName())
        filePathWithoutExtension = os.path.splitext(filePath)[0]
        newExtension = '.' + Config.get('handbrake.destination.extension')
        return filePathWithoutExtension + newExtension
