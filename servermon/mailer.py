"""mailer.py

contains functionality to send mail about server status to the admin
"""

from smtplib import SMTP_SSL
from email.message import Message
import datetime
import conf


def noop(smtp_object):
    return smtp_object.noop()


def login(smtp_object):
    return smtp_object.login(conf.SMTP_USER, conf.SMTP_PASSWORD)


def send_alert(smtp_object, body_text):
    message = Message()
    message['Resent-Date'] = str(datetime.datetime.now())
    message['Subject'] = 'ALERT: Server Down!'
    message.set_payload(body_text)

    return smtp_object.sendmail(
        conf.FROM_ADDRESS,
        conf.EMAIL_ADDRESS,
        message.as_string())
