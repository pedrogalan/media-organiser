from utils.FileUtils import FileUtils
#from entities.MediaBuilder import MediaBuilder
# from entities import Media

#filename = '/Users/pedro.galan/dev/my-projects/media-organiser/Media/samples/MEGA/2015-12-22_14.16.21_000003.jpg'
#filename = '/Users/pedro.galan/dev/my-projects/media-organiser/Media/samples/CameraDrop/other/deleteme.txt'
#filename = '/Users/pedro.galan/dev/my-projects/media-organiser/Media/samples/MEGA/death-list-five.jpg'


#print MediaBuilder.build(filename)

fullPath = '/Users/pedro.galan/dev/my-projects/media-organiser/Media/samples/MEGA/death-list-five.jpg'
destinationPath = '/Users/pedro.galan/dev/my-projects/media-organiser/Media/copied'
# FileUtils.move(fullPath, destinationPath)
#FileUtils.delete('/Users/pedro.galan/dev/my-projects/media-organiser/Media/copied/Pictures/2017/2017-03-06_11.44.19_000006.jpg')

#for filename in FileUtils.findFilesRecursivelly(destinationPath, tuple(['jpg']), 3):
#    print filename

FileUtils.removeDir(destinationPath)
