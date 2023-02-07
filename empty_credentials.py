import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 
import unittest
from dotenv import load_dotenv


load_dotenv()

email=''
password=''
browser=os.getenv('BROWSER')
LOGIN_URL = os.getenv('LOGIN_URL')


class EmptyCredentialsLogin(unittest.TestCase):
    def __init__(self, testname, email=email, password=password, browser='Chrome', driver=None):
        super().__init__(testname)
        self.email = email
        self.password = password
        self.browser = browser
        self.driver = driver

    def setUp(self):
        if self.browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif self.browser == 'Firefox':
            self.driver = webdriver.Firefox()
        self.driver.get(LOGIN_URL)
        time.sleep(1)
        time.sleep(2) 

    def test_empty_credentials_login(self):
        email = self.driver.find_element(By.ID, 'email')
        email.send_keys(self.email)

        password = self.driver.find_element(By.ID, 'pass')
        password.send_keys(self.password)

        login_button = self.driver.find_element(By.ID, 'loginbutton')
        login_button.click()

        # Explicit wait
        wait = WebDriverWait(self.driver, 10)
        error_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fsl.fwb.fcb")))

        if error_element:
            error_message = error_element.text
            self.assertEqual(error_message, "Wrong Credentials")
        else:
            self.assertFalse(False, "Login was successful.")

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    test_case = EmptyCredentialsLogin('test_empty_credentials_login', email, password, browser)
    unittest.main(argv=[''], exit=False)

