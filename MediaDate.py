from dateutil.parser import parse
from datetime import datetime

class MediaDate:

    def __init__(self, stringDate):
	# TODO Update the conversion string to date to make it robust
        s = self.__normaliseStringDate(stringDate)
	f = "%Y:%m:%d %H:%M:%S"
	self.date = datetime.strptime(s, f)

    def toFileName(self):
        return self.date.strftime('%Y-%m-%d_%H.%M.%S')

    def __normaliseStringDate(self, stringDate):
        if self.__hasTime(stringDate):
            return stringDate
        else:
            return stringDate + " 00:00:00Z"

    def __hasTime(self, stringDate):
        return " " in stringDate
