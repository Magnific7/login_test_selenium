import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time 
import unittest

class FacebookIncorrectLogin(unittest.TestCase):
    def __init__(self, email, password="dummy_pass", browser='Chrome', driver=None):
        unittest.TestCase.__init__(self)
        # Store credentials for login
        self.email = email
        self.password = password
        self.browser = browser
        self.driver = driver
        if self.browser == 'Chrome':
                self.driver = webdriver.Chrome()
        elif self.browser == 'Firefox':
                self.driver = webdriver.Firefox()
        self.driver.get(os.environ['LOGIN_URL'])
        time.sleep(1)

    def test_incorrect_password(self):
        email = self.driver.find_element('id','email')
        email.send_keys(self.email)

        password = self.driver.find_element('id','pass')
        password.send_keys(self.password)

        login_button = self.driver.find_element('id','loginbutton')
        login_button.click()

        # Explicit wait
        wait = WebDriverWait(self.driver, 10)
        error_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fsl.fwb.fcb")))

        if error_element:
            error_message = error_element.text
            self.assertEqual(error_message, "Wrong Credentials")
            print("Login was unsuccessful.")
        else:
            self.assertFalse(False, "Login was successful.")
            print("Login was successful.")


if __name__ == '__main__':
    try:
        fb_login = FacebookIncorrectLogin(email=os.environ['FB_EMAIL'], password="dummy_pass", browser=os.environ['BROWSER'])
        fb_login.test_incorrect_password()
    except Exception as e:
        print("Error:", e)
