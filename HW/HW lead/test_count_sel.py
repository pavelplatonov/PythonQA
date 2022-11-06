from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def test_simple():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get("http://selenium.dev")
