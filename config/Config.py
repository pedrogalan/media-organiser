from log.Logging import logging
from configparser import ConfigParser
from os.path import expanduser

def getConfigFileName():
    return expanduser("~") + '/.media-organiser'

def loadProperties():
    config = ConfigParser()
    try:
        with open(getConfigFileName()) as f:
            config.readfp(f)
    except IOError:
        createDefaultProperties()
        config.read(getConfigFileName())
    return config

def createDefaultProperties():
    file = open(getConfigFileName(), "w")
    file.write('[Pictures]\n')
    file.write('normaliser.path.sources.file.extensions = jpg,jpeg\n')
    file.write('normaliser.max.number.of.files=1000\n\n')
    file.write('renamer.path.sources.file.extensions = jpg,jpeg\n')
    file.write('renamer.max.number.of.files=1000\n\n')
    file.write('shrinker.path.sources.file.extensions = jpg,jpeg\n')
    file.write('shrinker.max.number.of.files=1000\n\n')
    file.write('classifier.path.sources.file.extensions = jpg,jpeg\n')
    file.write('classifier.max.number.of.files=1000\n\n')
    file.write('[Videos]\n')
    file.write('normaliser.path.sources.file.extensions = mov,3gp,avi,mkv,mp4\n')
    file.write('normaliser.max.number.of.files=1000\n\n')
    file.write('renamer.path.sources.file.extensions = mov,3gp,avi,mkv,mp4\n')
    file.write('renamer.max.number.of.files=1000\n\n')
    file.write('shrinker.path.sources.file.extensions = mov,3gp,avi,mkv,mp4\n')
    file.write('shrinker.max.number.of.files=50\n\n')
    file.write('classifier.path.sources.file.extensions = mov,3gp,avi,mkv,mp4\n')
    file.write('classifier.max.number.of.files=1000\n\n')
    file.write('[All]\n')
    file.write('normaliser.path.sources = /Users/john.doe/Camera Drop,/Users/john.doe/MEGA\n')
    file.write('normaliser.path.destination = /Users/john.doe/Media/normalised\n')
    file.write('normaliser.max.number.of.errors=1\n\n')
    file.write('renamer.path.sources = /Users/john.doe/Media/normalised\n')
    file.write('renamer.path.destination = /Users/john.doe/Media/renamed\n')
    file.write('renamer.max.number.of.errors=1\n\n')
    file.write('shrinker.path.sources = /Users/john.doe/Media/renamed\n')
    file.write('shrinker.path.destination = /Users/john.doe/Media/shrinked\n')
    file.write('shrinker.max.number.of.errors=1\n\n')
    file.write('classifier.path.sources = /Users/john.doe/Media/shrinked\n')
    file.write('classifier.path.destination = /Users/john.doe/Media/classified\n')
    file.write('classifier.max.number.of.errors=1\n\n')
    file.write('handbrake.profile=Very Fast 720p30\n')
    file.write('handbrake.destination.extension=mp4\n\n')
    file.write('log.file.location = /Users/john.doe/.media-organiser.log\n')
    file.close()

class Config:
    __properties = loadProperties()

    @staticmethod
    def get(name):
        try:
            return Config.getFromSection('All', name)
        except:
            logging.error("Configuration property %s not found in %s", name, getConfigFileName())

    @staticmethod
    def getFromSection(section, name):
        try:
            return Config.__properties.get(section, name)
        except:
            return Config.get(name)
