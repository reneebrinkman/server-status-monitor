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


def test_noop(smtp):
    assert mailer.noop(smtp)[0] == 250


def test_login(smtp):
    assert mailer.login(smtp)[0] == 235


def test_send_alert(authenticated_smtp):
    assert mailer.send_alert(authenticated_smtp, 'Test Alert') == {}
