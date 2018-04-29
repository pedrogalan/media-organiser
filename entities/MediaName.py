class MediaName:
    """Represents the name of a media which consists of a datetime plus a counter to prevent collisions."""

    def __init__(self, mediaDate):
        self.mediaDate = mediaDate
        self.counter = 0

    def getName(self):
        return self.mediaDate.toFileName() + '_' + str(self.counter).zfill(6)

    def getMediaDate(self):
        return self.mediaDate

    def getNextName(self):
        self.counter = self.counter + 1
        return self.getName()

    def __str__(self):
        return self.getName()
