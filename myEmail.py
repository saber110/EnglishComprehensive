
import config
import smtplib
from email.mime.text import MIMEText

class email:

    def __init__(self):
        self.user = config.emailuser
        self.pwd  = config.emailpwd
    
    def send(self, to, subject, text):
        msg = MIMEText(text)
        msg["Subject"] = subject
        msg["From"] =  self.user
        msg["To"] = to

        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(self.user, self.pwd)
            s.sendmail(self.user, to, msg.as_string())
            s.quit()
            print("Success!")
        except smtplib.SMTPException as e:
            print ("Falied,%s" %e)
    
    def sendAuto(self,text):
        for to in config.emailtouser:
            self.send(to, config.emailSubject, text)

# e = email()
# e.send("1428132225@qq.com", "english", "hahah")
# e.sendAuto("test")
