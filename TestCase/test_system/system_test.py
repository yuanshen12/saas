import pytest
from Locators.SystemLocators.subscribe_locators import SubscribeLocators as loc


class TestSystem():

    def test_01(self, start_module):
        self.driver = start_module
        loc(self.driver).get_subscribe("fend_start")
        assert 1 == 0


if __name__ == '__main__':
    pytest.main(["-s", "system_test.py"])

