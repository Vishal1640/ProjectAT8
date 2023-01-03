from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Note:
#Using time.sleep instead of implicit wait so that the step by step executions is visble

class create_emp():

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
        # Xpath for add
        xpath_for_add = '//i[@class="oxd-icon bi-plus oxd-button-icon"]'
        click_on_add = driver.find_element(By.XPATH, xpath_for_add)
        # Clicking on add
        click_on_add.click()
        # Xpath for first name
        xpath_for_first_name = '//input[@name="firstName"]'
        input_for_first_name = driver.find_element(By.XPATH, xpath_for_first_name)
        # Sending keys for first name
        input_for_first_name.send_keys("Vishal")
        # Xpath for last name
        xpath_for_last_name = '//input[@name="lastName"]'
        input_for_last_name = driver.find_element(By.XPATH, xpath_for_last_name)
        # Sending keys for last name
        input_for_last_name.send_keys("Balaji")
        time.sleep(3)
        # Xpath for clicking on login details
        xpath_for_enabling_login = '//p[normalize-space()="Create Login Details"]/following::div[1]'
        enabling_login = driver.find_element(By.XPATH, xpath_for_enabling_login)
        # Clicking on login
        enabling_login.click()
        time.sleep(3)
        # Xpath for entering username
        xpath_for_username = '//label[text()="Username"]/following::div[1]/input'
        enter_username = driver.find_element(By.XPATH, xpath_for_username)
        # Sending keys for username
        enter_username.send_keys("Vishal B")
        time.sleep(3)
        # Xpath for enabling
        xpath_for_enabling = '//label[normalize-space()="Enabled"]'
        clicking_on_enable = driver.find_element(By.XPATH, xpath_for_enabling)
        # Clicking on enable
        clicking_on_enable.click()
        #time.sleep(3)
        # Xpath for password
        xpath_for_pwd = '//label[normalize-space()="Password"]/following::div[1]/input'
        pwd_input = driver.find_element(By.XPATH, xpath_for_pwd)
        # Sending keys for password
        pwd_input.send_keys("Ripo@1640")
        time.sleep(3)
        # Xpath for confirming password
        xpath_for_confirming_pwd = '//label[normalize-space()="Confirm Password"]/following::div[1]/input'
        confirming_pwd_input = driver.find_element(By.XPATH, xpath_for_confirming_pwd)
        # Sending keys for password
        confirming_pwd_input.send_keys("Ripo@1640")
        time.sleep(3)
        # Clicking on save
        click_on_save = '//button[@type="submit"]'
        save_button = driver.find_element(By.XPATH, click_on_save)
        # Clicking on enable
        save_button.click()
        time.sleep(5)
        # Xpath for nickname
        xpath_for_nickname = '//label[normalize-space()="Nickname"]/following::div[1]/input'
        input_for_nickname = driver.find_element(By.XPATH, xpath_for_nickname)
        # Sending keys for nickname
        input_for_nickname.send_keys("Punter")
        time.sleep(3)
        # Xpath for other ID
        xpath_for_other_id = '//label[normalize-space() = "Other Id"]/following::div[1]/input'
        input_for_other_id = driver.find_element(By.XPATH, xpath_for_other_id)
        # Sending keys for other ID
        input_for_other_id.send_keys("1998")
        time.sleep(3)
        # Xpath for license expiry date
        xpath_for_exp_date = "(//input[@placeholder='yyyy-mm-dd'])[1]"
        click_on_exp_date = driver.find_element(By.XPATH, xpath_for_exp_date)
        # Sending keys for license expiry date
        click_on_exp_date.send_keys("2022-12-19")
        time.sleep(3)
        # Xpath for SSN no
        xpath_for_ssn_no = '//label[normalize-space()="SSN Number"]/following::div[1]/input'
        ssn_no_input = driver.find_element(By.XPATH, xpath_for_ssn_no)
        # Sending keys for SSN no
        ssn_no_input.send_keys("1640")
        time.sleep(3)
        # Xpath for SIN no
        xpath_for_sin_no = '//label[normalize-space()="SIN Number"]/following::div[1]/input'
        sin_no_input = driver.find_element(By.XPATH, xpath_for_sin_no)
        # Sending keys for SIN no
        sin_no_input.send_keys("0461")
        time.sleep(3)
        # Xpath for nationality
        xpath_for_nationality = '//label[normalize-space()="Nationality"]/following::div[1]'
        nationality_input = driver.find_element(By.XPATH, xpath_for_nationality)
        nationality_input.click()
        # Clicking on nationality
        clicking_on_nationality = '//div[@role="option"]/span[normalize-space()="Indian"]'
        nationality_click = driver.find_element(By.XPATH, clicking_on_nationality)       
        nationality_click.click()
        # Xpath for marital status
        xpath_for_marital_status = '//label[normalize-space()="Marital Status"]/following::div[1]'
        marital_status_input = driver.find_element(By.XPATH, xpath_for_marital_status)
        marital_status_input.click()
        # Clicking on marital status
        clicking_on_marital_status = '//div[@role="option"]/span[normalize-space()="Single"]'
        marital_status_click = driver.find_element(By.XPATH, clicking_on_marital_status)       
        marital_status_click.click()
        # Xpath for DOB
        xpath_for_dob = "(//input[@placeholder='yyyy-mm-dd'])[2]"
        click_on_dob = driver.find_element(By.XPATH, xpath_for_dob)
        # Sending keys for DOB
        click_on_dob.send_keys("1998-12-19")
        time.sleep(3)
        # Xpath for clicking on gender
        xpath_for_gender = '//label[normalize-space()="Male"]'
        click_on_gender = driver.find_element(By.XPATH, xpath_for_gender)
        # Clicking on gender
        click_on_gender.click()
        # Xpath for MS
        xpath_for_ms = '//label[normalize-space()="Military Service"]/following::div[1]/input'
        ms_input = driver.find_element(By.XPATH, xpath_for_ms)
        # Sending keys for MS
        ms_input.send_keys("No")
        time.sleep(3)
        # Xpath for clicking on save 1
        xpath_for_save_1 = '//p[text()=" * Required"]/following::button[@type="submit"][1]'
        click_on_save_1 = driver.find_element(By.XPATH, xpath_for_save_1)
        # Clicking on save 1
        click_on_save_1.click()
        time.sleep(3)
        # Xpath for blood type
        xpath_for_blood_type = '//label[normalize-space()="Blood Type"]/following::div[1]/div'
        blood_type_input = driver.find_element(By.XPATH, xpath_for_blood_type)
        blood_type_input.click()
        # Clicking on blood type
        clicking_on_blood_type = '//div[@role="option"]/span[normalize-space()="O+"]'
        blood_type_click = driver.find_element(By.XPATH, clicking_on_blood_type)       
        blood_type_click.click()
        # Xpath for clicking on save 2
        xpath_for_save_2 = '//label[normalize-space()="Blood Type"]/following::button[@type="submit"][1]'
        click_on_save_2 = driver.find_element(By.XPATH, xpath_for_save_2)
        # Clicking on save 1
        click_on_save_2.click()
        time.sleep(3)
        print("Employee is added successfully")
        driver.quit()
abc = create_emp()
abc.test()