from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Note:
#Using time.sleep instead of implicit wait so that the step by step executions is visble
class login():

    def test(self):

        baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # Initalizing the browser
        driver = webdriver.Firefox()
        driver.get(baseurl)
        # Maximzing the window
        driver.maximize_window()
        driver.implicitly_wait(10)
        # Xpath for username
        xpath_for_username = '//input[@name="username"]'
        username_enter = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_enter.send_keys("Admin")
        # Xpath for password
        xpath_for_password = '//input[@name="password"]'
        password_enter = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_enter.send_keys("admin123")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        clicking_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        clicking_on_login.click()
        print("The user logged in successfully")
        driver.quit()

abc = login()
abc.test()