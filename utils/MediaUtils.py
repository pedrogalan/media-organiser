class MediaUtils:

    @staticmethod
    def getMediaType(extension):
        pictureExtensions = ['jpg', 'jpeg', 'gif', 'png']
        videoExtensions = ['avi', 'mov', 'mp4', '3gp', 'mkv']
        if extension in pictureExtensions:
            return 'image'
        elif extension in videoExtensions:
            return 'video'
        else:
            return 'unknown'
