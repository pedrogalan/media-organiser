from Media import Media
from FileUtils import FileUtils
from glob import glob
from os.path import join

class Runner:

    def __init__(self, args):
        self.sourcePath = args[1]
        self.destinationPath = args[2]
        self.numberOfFilesRenamed = 0
        self.numberOfFilesToRename = self.__getMaxNumberOfFilesToRename(args)

    def run(self):
        for file in FileUtils.findFilesRecursivelly(self.sourcePath):
            self.__checkNumberOfFilesRenamed()
            self.__rename(file)

    def __getMaxNumberOfFilesToRename(self, args):
        try:
            return int(args[3])
        except:
            return 1000

    def __checkNumberOfFilesRenamed(self):
        if (self.numberOfFilesRenamed == self.numberOfFilesToRename):
            exit(0)
        self.numberOfFilesRenamed = self.numberOfFilesRenamed + 1

    def __rename(self, file):
        media = Media(file)
        FileUtils.mv(media, self.destinationPath)
