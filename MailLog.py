import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class MailLog:

    @staticmethod
    def sendLog():
       sender = 'pedro.calibre@gmx.com'
       receivers = ['lacimadelmundo@gmail.com']

       msg = MIMEMultipart()
       msg['From'] = sender
       msg['To'] = receivers[0]
       msg['Subject'] = 'simple email in python'
       message = 'here is the email'
       msg.attach(MIMEText(message))

       mailserver = smtplib.SMTP('mail.gmx.es')
       mailserver.login('pedro.calibre@gmx.com', 'Th1s1sGmx')
       mailserver.sendmail(sender, receivers, msg.as_string())
