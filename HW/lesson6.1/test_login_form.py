# import time

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.saucedemo.com/")


# def test_title():

#     title_from_site = driver.title
#     assert title_from_site == "Swag Labs"


# def test_login_form():
#     time.sleep(1)
#     # driver.find_element((By.CSS_SELECTOR, 'input#user-name'))
#     user_name = driver.find_element(By.ID, "user-name")
#     user_name.send_keys("standard_user")
#     time.sleep(1)

#     # password = driver.find_element(By.XPATH, "//input[contains(@placeholder, \'Password\')]")
#     password = driver.find_element(By.ID, "password")
#     password.send_keys("secret_sauce")
#     time.sleep(1)

#     # button_login = driver.find_element(By.XPATH, "//input[@name='login_button']")
#     button_login = driver.find_element(By.NAME, "login-button")
#     button_login.click()
#     time.sleep(1)

#     assert (
#         driver.current_url == "https://www.saucedemo.com/inventory.html"
#     ), "We reached another site!!!"

#     driver.quit
