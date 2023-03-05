from email.mime.text import MIMEText
import smtplib
from config import *


def send_email(content, subject, receiver_email):
    sender_email = mailName
    password = mailPassword

    message = MIMEText(content, "html")

    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()