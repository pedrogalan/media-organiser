import sys
sys.path.append('../entities')
from entities.MediaBuilder import MediaBuilder
from os.path import join
from os.path import basename
from os.path import isfile
from os.path import isdir
from os.path import exists
from os.path import dirname
from os import remove
from os import makedirs
from os import listdir
from os import rmdir
from os import walk
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
    def mv(sourceFilename, destinationPath):
        FileUtils.createDestinationDirectory(destinationPath)
        move(sourceFilename, destinationPath + '/')

    @staticmethod
    def copy(sourceFilename, destinationPath):
        media = MediaBuilder.build(sourceFilename)
        destinationFile = FileUtils.__prepareDestinationDirectory(media, destinationPath)
        copyfile(media.fullPath, destinationFile)

    @staticmethod
    def move(sourceFilename, destinationPath):
        media = MediaBuilder.build(sourceFilename)
        destinationFile = FileUtils.__prepareDestinationDirectory(media, destinationPath)
        move(media.fullPath, destinationFile)

    @staticmethod
    def delete(filePath):
        remove(filePath)

    @staticmethod
    def createDestinationDirectory(fullPath):
        dir = fullPath

        if basename(fullPath):
            dir = dirname(fullPath)

        if not exists(dir):
            try:
                makedirs(dirname(fullPath))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

    @staticmethod
    def removeDir(path):
        if not isdir(path):
            return
        entries = listdir(path)
        if len(entries):
            for entry in entries:
                fullpath = join(path, entry)
                if isdir(fullpath):
                    FileUtils.removeDir(fullpath)
        entries = listdir(path)
        if len(entries) == 0:
            rmdir(path)

    @staticmethod
    def getDestinationSubdirectory(media):
        year = media.getCreationYear()
        if media.isPicture():
            return join('Pictures', year)
        elif media.isVideo():
            return join('Videos', year)
        else:
            logging.error('The media type of %s is unknown.', media.fullPath)
            return join('Unknown', subdir)

    @staticmethod
    def __prepareDestinationDirectory(media, destinationPath):
        destinationFile = FileUtils.__getDestinationFilename(destinationPath, media)
        FileUtils.createDestinationDirectory(destinationFile)
        return destinationFile

    @staticmethod
    def __getDestinationFilename(destinationPath, media):
        destinationSubDirectory = FileUtils.getDestinationSubdirectory(media)
        fullDestinationPath = join(destinationPath, destinationSubDirectory)

        destinationFile = join(fullDestinationPath, media.getNextNewFileName())
        while isfile(destinationFile):
            destinationFile = join(fullDestinationPath, media.getNextNewFileName())

        return destinationFile
