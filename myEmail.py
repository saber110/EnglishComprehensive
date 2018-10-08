# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import config
import smtplib
from email.mime.text import MIMEText

class email:

    def __init__(self):
        self.user = config.emailuser
        self.pwd  = config.emailpwd

    def send(self, to, subject, text, type="plain", code="utf-8"):
        msg = MIMEText(text, type, code)
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

    def sendAuto(self,title,text):
        for to in config.emailtouser:
            self.send(to, title, text, "html")

# e = email()
# e.send("1428132225@qq.com", "english", "hahah")
# e.sendAuto("""g""")
