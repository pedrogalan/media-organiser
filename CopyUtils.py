from os.path import isfile
from shutil import copyfile
from shutil import move

class CopyUtils:

    @staticmethod
    def cp(media, destinationPath):
        destinationFile = CopyUtils.__getDestinationFilename(destinationPath, media)
        print "Copying " + media.sourceFile + " to " + destinationFile
        try:
            copyfile(media.sourceFile, destinationFile)
        except IOError, e:
            print "Error copying file." + e.errno

    @staticmethod
    def mv(media, destinationPath):
        destinationFile = CopyUtils.__getDestinationFilename(destinationPath, media)
        print "Moving " + media.sourceFile + " to " + destinationFile
        try:
            move(media.sourceFile, destinationFile)
        except IOError, e:
            print "Error moving file: " + str(e)

    @staticmethod
    def __getDestinationFilename(destinationPath, media):
        destinationFile = destinationPath + "/" + media.getNextNewFileName()
        while isfile(destinationFile):
            destinationFile = destinationPath + "/" + media.getNextNewFileName()
        return destinationFile
