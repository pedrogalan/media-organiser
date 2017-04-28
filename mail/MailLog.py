import sys
sys.path.append('../config')
from config.Config import Config
import smtplib

class MailLog:

    @staticmethod
    def sendLog():
        message = MailLog.__buildMessage()
        server = MailLog.__configureServer()
        server.sendmail(Config.get('mail.sender'), Config.get('mail.receiver'), message)
        server.quit()

    @staticmethod
    def __configureServer():
       mailserver = smtplib.SMTP(Config.get('mail.smtp.host'))
       mailserver.login(Config.get('mail.smtp.username'), Config.get('mail.smtp.password'))
       return mailserver

    @staticmethod
    def __buildMessage():
        template = 'From: {0}\nTo: {1}\nSubject: Something went wrong!\n{2}'
        return template.format(Config.get('mail.sender'), Config.get('mail.receiver'), MailLog.__readLogFile())

    @staticmethod
    def __readLogFile():
        try:
            f = open(Config.get('log.file.location'), 'r')
            return """\n""" + f.read()
        except:
            return """\nLog file cannot be found! Please, review your configuration."""
