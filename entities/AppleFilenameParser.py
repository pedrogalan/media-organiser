from . MediaName import MediaName
from . MediaDate import MediaDate

class AppleFilenameParser:

    @staticmethod
    def parse(filename):
        date = filename.replace('-', ':').replace('.', ':')[0:19]
        return MediaName(MediaDate(date, "Filename"))

