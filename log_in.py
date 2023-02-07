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
from dotenv import load_dotenv


load_dotenv()

email=os.getenv('FB_EMAIL')
password=os.getenv('FB_PASSWORD')
browser=os.getenv('BROWSER')
LOGIN_URL = os.getenv('LOGIN_URL')

class PageLogin(unittest.TestCase):
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

 

    def test_login(self):
        email_element = self.driver.find_element('id','email')
        email_element.send_keys(self.email)

        password_element = self.driver.find_element('id','pass')
        password_element.send_keys(self.password) 

        login_button = self.driver.find_element('id','loginbutton')
        login_button.click() 

        # Implicit wait
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_changes(self.driver.current_url))
        
        current_url = self.driver.current_url
        if "facebook.com/login" not in current_url:
            self.assertTrue(True, "Login was successful.")
        else:
            self.assertTrue(False, "Login was unsuccessful.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    test_case = PageLogin('test_login', email, password, browser)
    unittest.main(argv=[''], exit=False)
