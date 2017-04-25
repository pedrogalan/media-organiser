from dateutil.parser import parse

class MediaDate:

    def __init__(self, stringDate):
        self.date = parse(self.__normaliseStringDate(stringDate))

    def toFileName(self):
        return self.date.strftime('%Y-%m-%d_%H.%M.%S')

    def __normaliseStringDate(self, stringDate):
        if self.__hasTime(stringDate):
            return stringDate
        else:
            return stringDate + " 00:00:00Z"

    def __hasTime(self, stringDate):
        return " " in stringDate
