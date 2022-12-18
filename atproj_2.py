from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

# Test case 2:

class orangehrm():

    def test(self):

        # Giving the base url
        baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        # Intializing the driver

        driver = webdriver.Firefox()

        driver.get(baseurl)

        # Maximizing the window

        driver.maximize_window()

        driver.implicitly_wait(10)

        xpath_for_username = '//input[@name="username"]'

        username_input = driver.find_element(By.XPATH, xpath_for_username)

        # Sending keys to username

        username_input.send_keys("Admin")

        time.sleep(3)
    
        # Xpath for finding the password
        xpath_for_password = '//input[@type="password"]'

        password_input = driver.find_element(By.XPATH, xpath_for_password)

        # Sending keys to password

        password_input.send_keys("Vishal@1640")

        time.sleep(3)

        # Xpath for finding the log in

        xpath_for_login = '//button[@type="submit"]'

        click_on_login = driver.find_element(By.XPATH, xpath_for_login)

        # Sending keys to click on login

        click_on_login.click()

        time.sleep(3)

        # Xpath for getting error

        xpath_for_error_message = "//div[@class='oxd-alert oxd-alert--error']"

        error_message = driver.find_element(By.XPATH, xpath_for_error_message)

        print(error_message.text)

        
ff = orangehrm()

ff.test()