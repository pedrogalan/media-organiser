import Config
import smtplib

class MailLog:

    @staticmethod
    def sendLog():
        message = MailLog.__buildMessage()
        server = MailLog.__configureServer()
        server.sendmail(Config.mail_sender, Config.mail_receiver, message)
        server.quit()

    @staticmethod
    def __configureServer():
       mailserver = smtplib.SMTP(Config.mail_smtp_host)
       mailserver.login(Config.mail_smtp_username, Config.mail_smtp_password)
       return mailserver

    @staticmethod
    def __buildMessage():
        template = Config.mail_template
        return template.format(Config.mail_sender, Config.mail_receiver, MailLog.__readLogFile())

    @staticmethod
    def __readLogFile():
        try:
            f = open(Config.log_file_location, 'r')
            return """\n""" + f.read()
        except:
            return """\nLog file cannot be found! Please, review your configuration."""

MailLog.sendLog()
