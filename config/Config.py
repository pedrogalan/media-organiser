from ConfigParser import ConfigParser
from os.path import expanduser

def getConfigFileName():
    return expanduser("~") + '/.media-renamer'

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
    file.write("[all]\n\n")
    file.write("log.file.location=/change/me.log")
    file.close()

class Config:
    __properties = loadProperties()

    @staticmethod
    def get(name):
        try:
            return Config.__properties.get('all', name)
        except:
            logging.error("Configuration property %s not found in %s", name, getConfigFileName())
