import pytest
import requests


@pytest.fixture
def smtp_connection():
    return requests.get(url="http://sj.weileit.com/")