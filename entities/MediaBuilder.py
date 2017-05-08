from MediaBuilderFromMetaInfo import MediaBuilderFromMetaInfo
from MediaBuilderFromFilename import MediaBuilderFromFilename

class MediaBuilder:
    """It will create a media object from a media file. It will iterate over multiple builders:
            1. Try to create the media object with the information from the file name.
            2. Try to create the media object with the metainformation from the file.
    """

    @staticmethod
    def build(filename):
        builders = [MediaBuilderFromFilename(filename), MediaBuilderFromMetaInfo(filename)]
        for builder in builders:
            try:
                return builder.build()
            except:
                pass
        raise ValueError('Could not build media object from file ' + filename + '.')
