"""mailer.py

contains functionality to send mail about server status to the admin
"""

from email.message import Message
from smtplib import SMTP_SSL
import datetime
import conf


def create_message(subject, body_text):
    message = Message()
    message['Resent-Date'] = str(datetime.datetime.now())
    message['Subject'] = subject
    message.set_payload(body_text)

    return message


def noop(smtp_object):
    return smtp_object.noop()


def login(smtp_object):
    return smtp_object.login(conf.SMTP_USER, conf.SMTP_PASSWORD)

def send_message(smtp_object, message):
    return smtp_object.sendmail(
        conf.FROM_ADDRESS,
        conf.EMAIL_ADDRESS,
        message.as_string())

def send_alert(smtp_object, body_text):
    message = create_message(
        'ALERT: Server Down!',
        body_text)

    return send_message(smtp_object, message)

def send_report(smtp_object, body_text):
    message = create_message(
        'Routine Server Report',
        body_text)

    return send_message(smtp_object, message)
