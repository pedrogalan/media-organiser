from utils.NewFileUtils import NewFileUtils
#from entities.MediaBuilder import MediaBuilder
# from entities import NewMedia

#filename = '/Users/pedro.galan/dev/my-projects/media-organiser/Media/samples/MEGA/2015-12-22_14.16.21_000003.jpg'
#filename = '/Users/pedro.galan/dev/my-projects/media-organiser/Media/samples/CameraDrop/other/deleteme.txt'
#filename = '/Users/pedro.galan/dev/my-projects/media-organiser/Media/samples/MEGA/death-list-five.jpg'


#print MediaBuilder.build(filename)

fullPath = '/Users/pedro.galan/dev/my-projects/media-organiser/Media/samples/MEGA/death-list-five.jpg'
destinationPath = '/Users/pedro.galan/dev/my-projects/media-organiser/Media/copied'
# NewFileUtils.move(fullPath, destinationPath)
#NewFileUtils.delete('/Users/pedro.galan/dev/my-projects/media-organiser/Media/copied/Pictures/2017/2017-03-06_11.44.19_000006.jpg')

#for filename in NewFileUtils.findFilesRecursivelly(destinationPath, tuple(['jpg']), 3):
#    print filename

NewFileUtils.removeDir(destinationPath)
