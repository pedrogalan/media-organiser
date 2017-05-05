from fnmatch import filter
from os.path import isfile
from os.path import join
from os.path import exists
from os.path import dirname
from os import walk
from os import remove
from os import makedirs
from shutil import copyfile
from shutil import move

class FileUtils:

    @staticmethod
    def findFilesRecursivelly(sourcePath, extensions, maxNumberOfFiles):
        matches = []
        for root, dirnames, filenames in walk(sourcePath):
            for filename in filenames:
                if filename.lower().endswith(extensions):
                    matches.append(join(root, filename))
                    if len(matches) >= maxNumberOfFiles:
                        return matches
        return matches

    @staticmethod
    def copy(sourceFilename, destinationFilename):
        FileUtils.createDestinationDirectory(destinationFilename)
        copyfile(sourceFilename, destinationFilename)

    @staticmethod
    def move(sourceFilename, destinationFilename):
        FileUtils.createDestinationDirectory(destinationFilename)
        move(sourceFilename, destinationFilename)

    @staticmethod
    def rename(media, destinationPath):
        destinationFile = FileUtils.__getDestinationFilename(destinationPath, media)
        FileUtils.createDestinationDirectory(destinationFile)
        move(media.sourceFile, destinationFile)

    @staticmethod
    def delete(filePath):
        remove(filePath)

    @staticmethod
    def createDestinationDirectory(filename):
        if not exists(dirname(filename)):
            try:
                makedirs(dirname(filename))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

    @staticmethod
    def __getDestinationFilename(destinationPath, media):
        fullDestinationPath = join(destinationPath, FileUtils.__getDestinationSubdirectory(media))
        destinationFile = join(fullDestinationPath, media.getNextNewFileName())
        while isfile(destinationFile):
            destinationFile = join(fullDestinationPath, media.getNextNewFileName())
        return destinationFile

    @staticmethod
    def __getDestinationSubdirectory(media):
        subdir = media.getCreateYear()
        if media.isPicture():
            return join('Pictures', subdir)
        elif media.isVideo():
            return join('Videos', subdir)
        else:
            return join('Unknown', subdir)
