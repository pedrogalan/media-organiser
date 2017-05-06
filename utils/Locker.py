import tempfile
import os

def startService(serviceName):
    fullPath = __makeLockerPath(serviceName)
    if os.path.isfile(fullPath):
        return False
    open(fullPath, 'a').close()
    return True

def stopService(serviceName):
    fullPath = __makeLockerPath(serviceName)
    try:
        os.remove(fullPath)
    except:
        return True

def __makeLockerPath(serviceName):
    base = tempfile.gettempdir()
    filename = '.' + serviceName + '.lock'
    return os.path.join(base, filename)
