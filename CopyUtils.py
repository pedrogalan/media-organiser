from os.path import isfile
from shutil import copyfile
from shutil import move

class CopyUtils:

    @staticmethod
    def cp(media, destinationPath):
        destinationFile = CopyUtils.__getDestinationFilename(destinationPath, media)
        copyfile(media.sourcePath, destinationFile)

    @staticmethod
    def mv(media, destinationPath):
        destinationFile = CopyUtils.__getDestinationFilename(destinationPath, media)
        move(media.sourcePath, destinationFile)

    @staticmethod
    def __getDestinationFilename(destinationPath, media):
        destinationFile = destinationPath + "/" + media.getNextNewFileName()
        while isfile(destinationFile):
            destinationFile = destinationPath + "/" + media.getNextNewFileName()
        return destinationFile
