from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/ru/'

class TestMainPage():
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_1(self):
        self.driver.get(link)

    def test_2(self):
        self.driver.get(link)
        self.driver.find_element(By.XPATH, "//ul[@id = 'browse']//ul//a").click()

    def teardown(self):
        self.driver.quit()