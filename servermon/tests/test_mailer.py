from email.message import Message
from smtplib import SMTP_SSL
import pytest
import conf
from servermon import mailer


@pytest.fixture(scope='module')
def smtp():
    smtp_object = SMTP_SSL(conf.SMTP_SERVER)
    yield smtp_object
    smtp_object.quit()


@pytest.fixture
def authenticated_smtp(smtp):
    mailer.login(smtp)
    return smtp


def test_create_message():
    message = mailer.create_message('test', 'test')

    assert type(message) == Message
    assert type(message.get('Resent-Date')) == str
    assert type(message.get_payload()) == str


def test_noop(smtp):
    status_code, _ = mailer.noop(smtp)
    assert status_code == 250


def test_login(smtp):
    status_code, _ = mailer.login(smtp)
    assert status_code == 235


def test_send_message(authenticated_smtp):
    message = mailer.create_message('test', 'test')
    assert mailer.send_message(authenticated_smtp, message) == {}


def test_send_alert(authenticated_smtp):
    assert mailer.send_alert(authenticated_smtp, 'Test Alert') == {}


def test_send_report(authenticated_smtp):
    assert mailer.send_report(authenticated_smtp, 'Test Report') == {}
