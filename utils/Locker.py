import tempfile
import os

def startService():
    fullPath = __makeLockerPath('media-organiser')
    if os.path.isfile(fullPath):
        return False
    open(fullPath, 'a').close()
    return True

def stopService():
    fullPath = __makeLockerPath('media-organiser')
    try:
        os.remove(fullPath)
    except:
        return True

def __makeLockerPath(serviceName):
    base = tempfile.gettempdir()
    filename = '.' + serviceName + '.lock'
    return os.path.join(base, filename)
