import logging
from ConfigParser import ConfigParser
from os.path import expanduser

def loadProperties():
    # TODO Create default configuration file when it's not found
    config = ConfigParser()
    config.read(expanduser("~") + '/.media-organiser')
    return config

class Config:
    __properties = loadProperties()

    @staticmethod
    def get(name):
        try:
            return Config.__properties.get('all', name)
        except:
            logging.error("Configuration property %s not found in ~/.media-organiser.", name)
