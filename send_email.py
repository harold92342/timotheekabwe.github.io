import smtplib, ssl
import os

def send_email(message):

        host = "smtp.gmail.com"
        port = 465
        username = "timothekabwe@gmail.com"
        PASSWORD = os.getenv("PASSWORD")
        receiver = "timothekabwe@gmail.com"
        my_context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=my_context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)


