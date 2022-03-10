import pytest
from servermon import mailer

def test_noop():
    assert mailer.noop()[0] == 250
