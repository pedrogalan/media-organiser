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
        fullDestinationPath = join(destinationPath, FileUtils.__getDestinationSubdirectory(media))
        destinationFile = join(fullDestinationPath, media.getNextNewFileName())
        while isfile(destinationFile):
            destinationFile = join(destinationPath, media.getNextNewFileName())
        return destinationFile

    @staticmethod
    def __getDestinationSubdirectory(media):
        print media.type
        if media.isPicture():
            return "Pictures"
        elif media.isVideo():
            return "Videos"
        else:
            return "Unknown"
