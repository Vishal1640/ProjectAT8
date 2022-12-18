from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

# Test Case 5

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

        time.sleep(5)
    
        # Xpath for finding the password
        xpath_for_password = '//input[@type="password"]'

        password_input = driver.find_element(By.XPATH, xpath_for_password)

        # Sending keys to password

        password_input.send_keys("admin123")

        time.sleep(5)

        # Xpath for finding the log in

        xpath_for_login = '//button[@type="submit"]'

        click_on_login = driver.find_element(By.XPATH, xpath_for_login)

        # Sending keys to click on login

        click_on_login.click()

        time.sleep(5)

        # Xpath for switching to PIM tab

        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'

        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)

        time.sleep(5)

        switch_to_pim.click()

        time.sleep(5)

        #Xpath for deleting an account

        xpath_for_delete = '//button[@class="oxd-icon-button oxd-table-cell-action-space"]'

        delete_button = driver.find_element(By.XPATH, xpath_for_delete)

        #Clicking on delete icon

        delete_button.click()

        time.sleep(5)

        #Xpath for choosing ok

        xpath_for_ok = '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]'

        choosing_ok = driver.find_element(By.XPATH, xpath_for_ok)

        choosing_ok.click()

        time.sleep(5)


        print("Deleted an existing employee sccuessfully")

ff = orangehrm()

ff.test()



        
       
    
