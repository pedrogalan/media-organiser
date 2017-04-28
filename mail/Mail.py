import sys
sys.path.append('../config')
from config.Config import Config
import smtplib

class Mail:

    @staticmethod
    def sendMail(body):
        message = Mail.__buildMessage(body)
        server = Mail.__configureServer()
        server.sendmail(Config.get('mail.sender'), Config.get('mail.receiver'), message)
        server.quit()

    @staticmethod
    def __configureServer():
       mailserver = smtplib.SMTP(Config.get('mail.smtp.host'))
       mailserver.login(Config.get('mail.smtp.username'), Config.get('mail.smtp.password'))
       return mailserver

    @staticmethod
    def __buildMessage(body):
        template = 'From: {0}\nTo: {1}\nSubject: Something went wrong!\n{2}'
        return template.format(Config.get('mail.sender'), Config.get('mail.receiver'), body)
