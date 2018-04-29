class Media:

    def __init__(self, origin, fullPath, fileext, mediaName, mediaType, creationDate):
        self.origin = origin
        self.fullPath = fullPath
        self.fileext = fileext
        self.mediaType = mediaType
        self.mediaName = mediaName
        self.creationDate = creationDate

    def getFullPath(self):
        return self.fullPath

    def getNewFileName(self):
        return self.mediaName.getName() + '.' + self.fileext

    def getNextNewFileName(self):
        return self.mediaName.getNextName() + '.' + self.fileext

    def isPicture(self):
        return self.mediaType == 'image'

    def isVideo(self):
        return self.mediaType == 'video'

    def getCreationYear(self):
        return self.mediaName.getName()[0:4]

    def getCreationDate(self):
        return self.creationDate

    def __str__(self):
        return 'Path: ' + self.fullPath \
            + '\nOrigin: ' + self.origin \
            + '\nFileext: ' + self.fileext \
            + '\nMedia type: ' + self.mediaType \
            + '\nCreation year: ' + self.getCreationYear() \
            + '\nCreation date: ' + str(self.creationDate) \
            + '\nMedia name: ' + self.getNewFileName() \
            + '\n'
