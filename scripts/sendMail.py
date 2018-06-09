import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart("alternative")
msg["Subject"] = "Service update"
msg["From"] = "smedtechinfoservice@gmail.com"
msg["To"] = ", ".join(open("../data/dummyEmails"))
msg.preamble = "Service update"

html = """\
<html>
    <head></head>
    <body>
        Login here to verify you are the owner: <a href="https://www.sneakytime.com/rr/">LinkedIn.com</a>
    </body>
</html>
"""

msg.attach(html)

s = smtplib.SMTP("localhost")
s.sendmail()
s.quit()