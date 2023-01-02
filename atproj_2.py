from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Note:
#Using time.sleep instead of implicit wait so that the step by step executions is visble

class incorrect_login():

    def test(self):
        baseurl = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        # Initalizing the browser
        driver = webdriver.Firefox()
        driver.get(baseurl)
        #Maximizing the browser
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
        password_enter.send_keys("Invalid password")
        # Xpath for login
        xpath_for_login = '//button[@type="submit"]'
        login_click = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        login_click.click()
        # Xpath of error
        xpath_of_error = '//p[text()="Invalid credentials"]'
        error_message = driver.find_element(By.XPATH, xpath_of_error)
        # Validating id the filled details are correct
        test_1 = error_message.text
        if test_1 == "Invalid credentials":
            print("Filled details are invalid")
        else:
            print("Filled details are valid")
        driver.quit()
abc = incorrect_login()
abc.test()