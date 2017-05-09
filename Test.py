from entities.DefaultFilenameParser import DefaultFilenameParser
from entities.SamsungFilenameParser import SamsungFilenameParser
from entities.MotorolaFilenameParser import MotorolaFilenameParser

filename = '2014-09-05 11.22.43.jpg'

try:
    print DefaultFilenameParser.parse(filename).getName()
except:
    pass

try:
    print SamsungFilenameParser.parse(filename).getName()
except:
    pass

try:
    print MotorolaFilenameParser.parse(filename).getName()
except:
    pass
