"""mailer.py

contains functionality to send mail about server status to the admin
"""

from smtplib import SMTP_SSL
import conf


def noop():
    with SMTP_SSL(conf.SMTP_SERVER) as smtp:
        return smtp.noop()
