import pytest


def test_01():
    name = 9
    return name

def test_02():
    name = 4
    assert name == test_01()

if __name__ == '__main__':
    pytest.main('')