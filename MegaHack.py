import os
from utils.FileUtils import FileUtils
from config.Config import Config

class DateName:
    def __init__(self, year, month, day, hour, minute, second, counter, path, filename, fileext):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.counter = counter
        self.path = path
        self.filename = filename
        self.fileext = fileext

    @staticmethod
    def fromName(name):
        path, file = os.path.split(name)
        extension = file.split('.')[-1].lower()
        dateAndCounterFromName = file.split('_')
        dateFromName = dateAndCounterFromName[0]

        if (len(dateAndCounterFromName) == 2):
            counter = dateAndCounterFromName[1].split('.')[0]
        else:
            counter = '1'

        dateTime = dateFromName.split(' ')
        date = dateTime[0]
        time = dateTime[1]

        year = date.split('-')[0]
        month = date.split('-')[1]
        day = date.split('-')[2]

        hour = time.split('.')[0]
        minute = time.split('.')[1]
        second = time.split('.')[2]

        return DateName(year, month, day, hour, minute, second, counter, path, file, extension)

    def getDate(self):
        return self.year + '-' + self.month + '-' + self.day + '_' + self.hour + '.' + self.minute + '.' + self.second

    def getFinalName(self):
        return os.path.join(self.path, self.getDate() + '_' + str(self.counter).zfill(6) + '.' + self.fileext)

    def getOriginalName(self):
        return os.path.join(self.path, self.filename)

    def rename(self):
        print 'Moving file ' + self.getOriginalName() + ' to: ' + self.getFinalName()
        # FileUtils.copy(self.getOriginalName(), self.getFinalName())

extensions = tuple(Config.getFromSection('Pictures', 'renamer.path.sources.file.extensions').split(','))
files = FileUtils.findFilesRecursivelly('Media/samples', extensions, 10)

for file in files:
    try:
        DateName.fromName(file).rename()
    except:
        print 'Could not parse ' + os.path.basename(file)
