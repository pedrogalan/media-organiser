import sys
sys.path.append('../config')
from config.Config import Config
sys.path.append('../mail')
from mail.MailLog import MailLog

class ErrorChecker:

    @staticmethod
    def check():
        if ErrorChecker.__areThereErrors():
            MailLog.sendLog()
            print "Clearing log file."

    @staticmethod
    def __areThereErrors():
        if '[ERROR]' in open(Config.get('log.file.location')).read():
            return True
        return False
