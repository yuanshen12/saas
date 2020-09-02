# ./test_smtpsimple.py
import pytest


def test_ehlo(smtp_connection):
    response = smtp_connection
    assert response == 250
    assert 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])
