from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

# Test Case 3:

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

        # Xpath for switching to PIM tab

        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'

        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)

        switch_to_pim.click()

        # Xpath for clicking on Add button

        xpath_for_add = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'

        click_on_add = driver.find_element(By.XPATH, xpath_for_add)

        click_on_add.click()

        time.sleep(3)

        # Sending input for first name

        xpath_for_first_name = '//input[@placeholder="First Name"]'

        enter_first_name = driver.find_element(By.XPATH, xpath_for_first_name)

        # Sending keys for first name

        enter_first_name.send_keys("Ricky")

        time.sleep(3)

        # Sending input for middle name

        xpath_for_middle_name = '//input[@placeholder="Middle Name"]'

        enter_middle_name = driver.find_element(By.XPATH, xpath_for_middle_name)

        # Sending keys for middle name

        enter_middle_name.send_keys("Thomas")

        time.sleep(3)

        # Sending input for last name

        xpath_for_last_name = '//input[@placeholder="Last Name"]'

        enter_last_name = driver.find_element(By.XPATH, xpath_for_last_name)

       # Sending keys for last name

        enter_last_name.send_keys("Hughes")

        time.sleep(3)

        # Finding xpath for save button

        xpath_for_save_button = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'

        save_button = driver.find_element(By.XPATH, xpath_for_save_button)

        # Clicking on save button 

        save_button.click()

        time.sleep(10)

        # Findin xpath for nickname

        xpath_for_nickname = '//label[text()="Nickname"]/following::div[1]/input'

        nickname_given = driver.find_element(By.XPATH, xpath_for_nickname)

        # Sending keys for nickname

        nickname_given.send_keys("trpnop")

        time.sleep(5)

        # Finding xpath for other ID

        xpath_for_other_id = '//label[text()="Other Id"]/following::div[1]/input'

        other_id = driver.find_element(By.XPATH, xpath_for_other_id) 

        # Sending keys for other ID

        other_id.send_keys("1640")

        time.sleep(5)

        # Finding xpath for Driving license

        xpath_for_license = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'

        driving_license = driver.find_element(By.XPATH, xpath_for_license)

        # Sending keys for Driving license

        driving_license.send_keys("79910602")

        time.sleep(5)

        # Finding xpath for Driving license date

        xpath_for_license_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'

        license_date = driver.find_element(By.XPATH, xpath_for_license_date)

        # Sending keys for driving license date

        license_date.send_keys("2026-12-19")

        time.sleep(5)

        # Finding xpath for SSN number

        xpath_for_ssn = '//label[text()="SSN Number"]/following::div[1]/input'

        ssn_no = driver.find_element(By.XPATH, xpath_for_ssn)

        # Sending keys for SSN no

        ssn_no.send_keys("7991")

        time.sleep(5)

        # Finding xpath for SIN number

        xpath_for_sin = '//label[text()="SIN Number"]/following::div[1]/input'

        sin_no = driver.find_element(By.XPATH, xpath_for_sin)

        # Sending keys for SIN no

        sin_no.send_keys("12345")

        time.sleep(5)

        # # Finding xpath for nationality

        # xpath_for_nationality = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'

        # nationality_selection = driver.find_element(By.XPATH)

        # # Sending keys for nationality

        # nationality_selection.send_keys("Indian")

        # time.sleep(5)

        # # Finding xpath for marital status

        # xpath_for_marital = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div'

        # marital_status = driver.find_element(By.XPATH, xpath_for_marital)

        # # Sending keys for matiral status

        # marital_status.send_keys("Single")

        # time.sleep(5)

        # Finding xpath for DOB

        xpath_for_dob = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'

        dob_selection = driver.find_element(By.XPATH, xpath_for_dob)

        # Sending keys for DOB

        dob_selection.send_keys("1997-06-12")

        time.sleep(5)

        # Finding xpath for Gender

        xpath_for_gender = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'

        gender_selection = driver.find_element(By.XPATH, xpath_for_gender)

        gender_selection.click()

        time.sleep(5)

        # Finding xpath for Military selection

        xpath_for_ms = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'

        ms_selection = driver.find_element(By.XPATH, xpath_for_ms)

        # Sending keys for MS

        ms_selection.send_keys("No")

        time.sleep(5)

        # Finding xpath for Smoker

        xpath_for_smoking = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label'

        smoking_habit = driver.find_element(By.XPATH, xpath_for_smoking)

        # Clicking on smoke radio button

        smoking_habit.click()

        time.sleep(5)

        # Finding xpath for save

        xpath_for_saving = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'

        saving_button = driver.find_element(By.XPATH, xpath_for_saving)

        # Clicking on save button

        saving_button.click()

        time.sleep(5)

        print("Filled in the personal details successfully")

ff = orangehrm()

ff.test()

