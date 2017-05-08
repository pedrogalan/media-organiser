from entities.MediaBuilderFromMetaInfo import MediaBuilderFromMetaInfo
from entities.MediaBuilderFromFilename import MediaBuilderFromFilename

filename = '/Users/pedro.galan/dev/my-projects/media-organiser/Media/samples/MEGA/2015-12-22_14.16.21_000003.jpg'
# filename = '/Users/pedro.galan/dev/my-projects/media-organiser/Media/samples/CameraDrop/other/deleteme.txt'

print MediaBuilderFromMetaInfo(filename).build()
print MediaBuilderFromFilename(filename).build()
