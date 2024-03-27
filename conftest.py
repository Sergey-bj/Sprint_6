import pytest
from selenium import webdriver
from constants import Constants

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Constants.URL)
    yield driver
    driver.quit()