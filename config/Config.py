from log.Logging import logging
from ConfigParser import ConfigParser
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
    # TODO Complete when all parameters work
    file = open(getConfigFileName(), "w")
    file.write('[all]\n\n')
    file.write('renamer.path.sources=/change/me,/also/change/me\n')
    file.write('renamer.path.destination=/change/me\n')
    file.write('renamer.path.sources.file.extensions=jpg,jpeg,mov,3gp,avi,mkv,mp4')
    file.write('renamer.max.number.of.files=1000\n')
    file.write('renamer.max.number.of.errors=5\n\n')
    file.write('shrinker.path.sources=/change/me\n')
    file.write('shrinker.path.destination=/change/me\n')
    file.write('shrinker.path.sources.file.extensions=jpg,jpeg,mov,3gp,avi,mkv,mp4')
    file.write('shrinker.max.number.of.files=1000\n')
    file.write('shrinker.max.number.of.errors=5\n\n')
    file.write('handbrake.profile=profile\n')
    file.write('handbrake.destination.extension=mp4\n\n')
    file.write('classifier.path.sources=/change/me\n')
    file.write('classifier.path.destination=/change/me\n')
    file.write('classifier.path.sources.file.extensions=jpg,jpeg,mov,3gp,avi,mkv,mp4')
    file.write('classifier.max.number.of.files=1000\n')
    file.write('classifier.max.number.of.errors=5\n\n')
    file.write('log.file.location=/change/me.log')
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
