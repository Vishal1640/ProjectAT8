from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Note:
#Using time.sleep instead of implicit wait so that the step by step executions is visble

class delete_emp():

    def test(self):
        baseurl = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        # Initaliazing the browser
        driver = webdriver.Firefox()
        driver.get(baseurl)
        driver.implicitly_wait(10)
        # xpath for username
        xpath_for_username = '//input[@name="username"]'
        username_input = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        username_input.send_keys("Admin")
        # Xpath for password
        xpath_for_password = '//input[@name="password"]'
        password_input = driver.find_element(By.XPATH, xpath_for_password)
        # Sending keys for password
        password_input.send_keys("admin123")
        # Xpath for clicking on login
        xpath_for_login = '//button[@type="submit"]'
        clicking_on_login = driver.find_element(By.XPATH, xpath_for_login)
        # Clicking on login
        clicking_on_login.click()
        # Switching to PIM tab
        xpath_for_PIM = '//a[@href="/web/index.php/pim/viewPimModule"]'
        switch_to_PIM = driver.find_element(By.XPATH, xpath_for_PIM)
        # Clicking on PIM
        switch_to_PIM.click()
        time.sleep(3)
        # Xpath for searching emp name
        xpath_for_searching_emp_name = '//label[text()="Employee Name"]/following::div[2]/div/input'
        searching_emp_name = driver.find_element(By.XPATH, xpath_for_searching_emp_name)
        # Sending keys for emp name
        searching_emp_name.send_keys("Vishal Balaji")
        time.sleep(3)
        # Xpath for clicking on search
        xpath_for_search = '//button[@type="submit"]'
        clicking_on_search = driver.find_element(By.XPATH, xpath_for_search)
        # Clicking on search
        clicking_on_search.click()
        time.sleep(3)
        # Xpath for deleting
        xpath_for_deleting = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][1]'
        clicking_on_deleting = driver.find_element(By.XPATH, xpath_for_deleting)
        # Clicking on deleting
        clicking_on_deleting.click()
        # Choosing on deleting
        delete_option = '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]'
        choosing_delete = driver.find_element(By.XPATH, delete_option)
        # Clicking on deleting
        choosing_delete.click()
        time.sleep(3)
        print("Deleted an existing employee sccuessfully")
        driver.quit()
abc = delete_emp()
abc.test()       
    
