import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from data.emailCreds import *

def sendMail():

    msg = MIMEMultipart("alternative")
    recipients = "".join(open("../data/dummyEmails"))
    msg["Subject"] = "Service update"
    msg["From"] = getEmail()
    msg["To"] = recipients
    # msg["To"] = "soer8617@stud.kea.dk" #Only for testing. The line above is the one to be used
    msg.preamble = "Service update"

    html = """\
    <html>
        <head></head>
        <body>
            <p>We have recently detected unnatural activity from your LinkedIn profile.</p>
            <p>We need you to prove you are the owner, so we can see if any other mismatching</p>
            <p>IP's have tried to or have had access to your account.</p>
            Login here to verify you are the owner: <a href="https://www.sneakytime.com/rr/">www.LinkedIn.com</a>
        </body>
    </html>
    """

    # string_text = "Testing message"

    msg.attach(MIMEText(html, "html"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(getEmail(), getPass())
        server.sendmail(getEmail(), recipients.split(), msg.as_string())
        server.quit()
        print("Succeeded in sending mail.")

    except:
        print("Failed to send mail")