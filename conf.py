"""conf.py

The configuration file for the app
"""

# put the email address of the server admin here
EMAIL_ADDRESS = 'reneebrinkman91@gmail.com'

# your server for sending email
SMTP_SERVER = 'smtp.gmail.com'

# These are the servers the app should check.
# Each entry in the list takes the following form:
# tuple(hostname, port)
SERVERS = [
    ('github.com', 443),
    ('github.com', 22),
    ('python.org', 443)
]
