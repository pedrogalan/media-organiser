import logging
from Media import Media
from FileUtils import FileUtils
from glob import glob
from os.path import join

class Runner:
    MAX_NUMBER_OF_FILES_TO_RENAME = 1000

    def __init__(self, args):
        self.sourcePath = args[1]
        self.destinationPath = args[2]
        self.numberOfFilesToRename = self.__getMaxNumberOfFilesToRename(args)

    def run(self):
        for file in FileUtils.findFilesRecursivelly(self.sourcePath, self.numberOfFilesToRename):
            try:
                self.__rename(file)
            except:
                logging.error("Error renaming %s.", str(file), exc_info=True)

    def __getMaxNumberOfFilesToRename(self, args):
        try:
            return int(args[3])
        except:
            return Runner.MAX_NUMBER_OF_FILES_TO_RENAME

    def __rename(self, file):
        media = Media(file)
        FileUtils.cp(media, self.destinationPath)
