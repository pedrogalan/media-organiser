class NewMedia:

    def __init__(self, fullPath, path, filename, fileext, mediaName, mediaType):
        self.fullPath = fullPath
        self.path = path # TODO delete me?
        self.filename = filename # TODO delete me?
        self.fileext = fileext
        self.mediaType = mediaType
        self.mediaName = mediaName

    def getNewFileName(self):
        return self.mediaName.getName() + '.' + self.fileext

    def getNextNewFileName(self):
        return self.mediaName.getNextName() + '.' + self.fileext

    def isPicture(self):
        return self.type == 'image'

    def isVideo(self):
        return self.type == 'video'

    def getCreationYear(self):
        return self.mediaName.getName()[0:4]

    def __str__(self):
        return 'Path: ' + self.fullPath \
            + '\nFileext: ' + self.fileext \
            + '\nMedia type: ' + self.mediaType \
            + '\nCreation year: ' + self.getCreationYear() \
            + '\nMedia name: ' + self.getNewFileName() \
            + '\n'
