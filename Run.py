from sys import argv, exit
from Media import Media
from CopyUtils import CopyUtils
from glob import glob

if len(argv) < 3 or len(argv) > 4:
    print "Usage: " + argv[0] + " source-path destination-path [max-files-to-rename]"
    exit(1)

sourcePath = argv[1]
destinationPath = argv[2]
if len(argv) == 4:
    maxFiles = argv[3]

for file in glob(sourcePath + "/*"):
    media = Media(file)
    CopyUtils.mv(media, destinationPath)
