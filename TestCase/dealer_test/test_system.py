import pytest
from Locators.DealerLocators.dealersystem import SystemLocators as loc


class TestSystem():

    def test_06(self, dealer_session_login):
        self.driver = dealer_session_login
        reagent = loc(self.driver).system_tissue()
        assert reagent is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_01.py'])