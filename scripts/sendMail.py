import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from data.emailCreds import *

msg = MIMEMultipart("alternative")
msg["Subject"] = "Service update"
msg["From"] = getEmail()
#msg["To"] = ", ".join(open("../data/dummyEmails"))
msg["To"] = "soer8617@stud.kea.dk" #Only for testing. The line above is the one to be used
msg.preamble = "Service update"

html = """\
<html>
    <head></head>
    <body>
        <p>We have recently detected unnatural activity from your LinkedIn profile.</p>
        <p>We need you to prove you are the owner, so we can see if any other mismatching</p>
        <p>IP's have tried to or have had access to your account.</p>
        Login here to verify you are the owner: <a href="https://www.sneakytime.com/rr/">LinkedIn.com</a>
    </body>
</html>
"""

string_text = "Søren er en luder"

msg.attach(MIMEText(string_text))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(getEmail(), getPass())
    server.sendmail('no-reply@gofuckyourself.com', msg["To"], msg.as_string())
    server.quit()
    print("Succeeded in sending mail.")

except:
    print("Failed to send mail")