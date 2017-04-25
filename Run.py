from sys import argv, exit
from Media import Media
from FileUtils import FileUtils
from glob import glob
from os.path import join

def __checkNumberOfFilesHandled(current, max):
    if (current == max):
        exit(0)
    return current + 1



if len(argv) < 3 or len(argv) > 4:
    print "Usage: " + argv[0] + " source-path destination-path [max-files-to-rename]"
    exit(1)

sourcePath = argv[1]
destinationPath = argv[2]
if len(argv) == 4:
    maxFiles = int(argv[3])
else:
    maxFiles = -1
numberOfRenamedFiles = 0

for file in glob(join(sourcePath, "*")):
    numberOfRenamedFiles = __checkNumberOfFilesHandled(numberOfRenamedFiles, maxFiles)

    media = Media(file)
    FileUtils.mv(media, destinationPath)
