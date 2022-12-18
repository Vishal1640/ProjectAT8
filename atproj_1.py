from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

# Test case 1:


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

        

        # Xpath for finding the username

        xpath_for_username = '//input[@name="username"]'

        username_input = driver.find_element(By.XPATH, xpath_for_username)

        # Sending keys to username

        username_input.send_keys("Admin")

        time.sleep(3)


        # Xpath for finding the password

        xpath_for_password = '//input[@type="password"]'

        password_input = driver.find_element(By.XPATH, xpath_for_password)

        # Sending keys to password

        password_input.send_keys("admin123")

        time.sleep(3)

        # Xpath for finding the log in

        xpath_for_login = '//button[@type="submit"]'

        click_on_login = driver.find_element(By.XPATH, xpath_for_login)

        # Sending keys to click on login

        click_on_login.click()

        time.sleep(3)

        print("The user is logged in successfully")

ff = orangehrm()

ff.test()



