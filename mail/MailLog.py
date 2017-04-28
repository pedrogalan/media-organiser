import sys
sys.path.append('../config')
from config.Config import Config
from Mail import Mail

class MailLog:

    @staticmethod
    def sendLog():
        body = MailLog.__readLogFile()
        Mail.sendMail(body)

    @staticmethod
    def __readLogFile():
        try:
            f = open(Config.get('log.file.location'), 'r')
            return """\n""" + f.read()
        except:
            return """\nLog file cannot be found! Please, review your configuration."""
