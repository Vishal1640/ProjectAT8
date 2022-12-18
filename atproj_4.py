from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

# Test Case 4:

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

    
        # Xpath for finding the password
        
        xpath_for_password = '//input[@type="password"]'

        password_input = driver.find_element(By.XPATH, xpath_for_password)

        # Sending keys to password

        password_input.send_keys("admin123")

        # Xpath for finding the log in

        xpath_for_login = '//button[@type="submit"]'

        click_on_login = driver.find_element(By.XPATH, xpath_for_login)

        # Sending keys to click on login

        click_on_login.click()

        # Finding Xpath for switching to PIM tab

        xpath_for_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'

        switch_to_pim = driver.find_element(By.XPATH, xpath_for_pim)

        switch_to_pim.click()

        # Finding xpath for editing employee

        xpath_for_emp = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[5]/div'

        emp_name = driver.find_element(By.XPATH, xpath_for_emp)

        # Clicking on emp name

        emp_name.click()

        time.sleep(10)

        # Finding xpath for nickname

        xpath_for_nickname = '//label[text()="Nickname"]/following::div[1]/input'

        nickname_given = driver.find_element(By.XPATH, xpath_for_nickname)
        
        # Clearing existing data

        nickname_given.send_keys(Keys.CONTROL,'a')

        nickname_given.send_keys(Keys.BACKSPACE)

        time.sleep(5)

        # Sending keys for nickname

        nickname_given.send_keys("ponrtp")

        time.sleep(5)

        # Finding xpath for other ID

        xpath_for_other_id = '//label[text()="Other Id"]/following::div[1]/input'

        other_id = driver.find_element(By.XPATH, xpath_for_other_id) 

        # Clearing existing data

        other_id.send_keys(Keys.CONTROL,'a')

        other_id.send_keys(Keys.BACKSPACE)

        time.sleep(5)

        # Sending keys for other ID

        other_id.send_keys("0416")

        time.sleep(5)

        # Finding xpath for Driving license

        xpath_for_license = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'

        driving_license = driver.find_element(By.XPATH, xpath_for_license)

        # Clearing existing data

        driving_license.send_keys(Keys.CONTROL,'a')

        driving_license.send_keys(Keys.BACKSPACE)

        time.sleep(5)

        # Sending keys for Driving license

        driving_license.send_keys("02061997")

        time.sleep(5)

        # Finding xpath for Driving license date

        xpath_for_license_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'

        license_date = driver.find_element(By.XPATH, xpath_for_license_date)

        # Clearing existing data

        license_date.send_keys(Keys.CONTROL,'a')

        license_date.send_keys(Keys.BACKSPACE)

        time.sleep(5)

        # Sending keys for driving license date

        license_date.send_keys("2027-12-19")

        time.sleep(5)

        # Finding xpath for SSN number

        xpath_for_ssn = '//label[text()="SSN Number"]/following::div[1]/input'

        ssn_no = driver.find_element(By.XPATH, xpath_for_ssn)

        # Clearing existing data

        ssn_no.send_keys(Keys.CONTROL,'a')

        ssn_no.send_keys(Keys.BACKSPACE)

        time.sleep(5)

        # Sending keys for SSN no

        ssn_no.send_keys("1997")

        time.sleep(5)

        # Finding xpath for SIN number

        xpath_for_sin = '//label[text()="SIN Number"]/following::div[1]/input'

        sin_no = driver.find_element(By.XPATH, xpath_for_sin)

        # Clearing existing data

        sin_no.send_keys(Keys.CONTROL,'a')

        sin_no.send_keys(Keys.BACKSPACE)

        time.sleep(5)

        # Sending keys for SIN no

        sin_no.send_keys("54321")

        time.sleep(5)

        # # Finding xpath for nationality

        # xpath_for_nationality = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'

        # nationality_selection = driver.find_element(By.XPATH)

        # # Sending keys for nationality

        # nationality_selection.send_keys("Australian")

        # time.sleep(5)

        # # Finding xpath for marital status

        # xpath_for_marital = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div'

        # marital_status = driver.find_element(By.XPATH, xpath_for_marital)

        # # Sending keys for matiral status

        # marital_status.send_keys("Married")

        # time.sleep(5)

        # Finding xpath for DOB

        xpath_for_dob = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'

        dob_selection = driver.find_element(By.XPATH, xpath_for_dob)

        # Clearing existing data

        dob_selection.send_keys(Keys.CONTROL,'a')

        dob_selection.send_keys(Keys.BACKSPACE)

        time.sleep(5)

        # Sending keys for DOB

        dob_selection.send_keys("1998-06-12")

        time.sleep(5)

        # Finding xpath for Gender

        xpath_for_gender = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'

        gender_selection = driver.find_element(By.XPATH, xpath_for_gender)

        gender_selection.click()

        time.sleep(5)

        # Finding xpath for Military selection

        xpath_for_ms = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'

        ms_selection = driver.find_element(By.XPATH, xpath_for_ms)

        # Clearing existing data

        ms_selection.send_keys(Keys.CONTROL,'a')

        ms_selection.send_keys(Keys.BACKSPACE)

        time.sleep(5)

        # Sending keys for MS

        ms_selection.send_keys("Yes")

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

        print("Employee data has been edited successfully")

ff = orangehrm()

ff.test()