import pytest
import smtplib


def test_ehlo(smtp_connection):
    response = smtp_connection
    assert response == 250
    # assert 0 # for debug


def test_noop(smtp_connection):
    response = str(smtp_connection)
    assert str(200) in response
    # assert 0 # for debug

