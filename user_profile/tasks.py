import smtplib, ssl
from email import encoders
from email.mime.text import MIMEText

from celery import shared_task

url = "http://127.0.0.1:8000/"



@shared_task
def send_welcome_mail(user):
    body = """
    Hello %s,
    welcome to our website, you can do login now 
    Link: %slogin/

    Thank You,
    """% (user.username, url)

    subject = "Welcome Email"
    recipients = [user.email]

    try:
        send_email(body, subject, recipients)
        return "Email was sent"
    except Exception as e:
        print("email not sent", e)



def send_email(body, subject, recipients, body_type='plain'):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls() 
    server.login("example@gmail.com", "123456")
    sender = "example.gmail.com"
    message = MIMEText(body, body_type)
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = ', '.join(recipient)
    server.sendmail(sender, recepinect, message.as_string())
