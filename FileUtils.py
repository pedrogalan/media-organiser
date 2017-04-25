from os.path import isfile
from os.path import join
from shutil import copyfile
from shutil import move

class FileUtils:

    @staticmethod
    def cp(media, destinationPath):
        destinationFile = FileUtils.__getDestinationFilename(destinationPath, media)
        print "Copying " + media.sourceFile + " to " + destinationFile
        try:
            copyfile(media.sourceFile, destinationFile)
        except IOError, e:
            print "Error copying file." + e.errno

    @staticmethod
    def mv(media, destinationPath):
        destinationFile = FileUtils.__getDestinationFilename(destinationPath, media)
        print "Moving " + media.sourceFile + " to " + destinationFile
        try:
            move(media.sourceFile, destinationFile)
        except IOError, e:
            print "Error moving file: " + str(e)

    @staticmethod
    def __getDestinationFilename(destinationPath, media):
        destinationFile = join(destinationPath, media.getNextNewFileName())
        while isfile(destinationFile):
            destinationFile = join(destinationPath, media.getNextNewFileName())
        return destinationFile

    def __normalisePath(path):
        return path.strip("/")
