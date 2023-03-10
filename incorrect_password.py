import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time 
import unittest
from dotenv import load_dotenv


load_dotenv()

email=os.getenv('FB_EMAIL')
password=os.getenv('INCORRECT_PASSWORD')
browser=os.getenv('BROWSER')
LOGIN_URL = os.getenv('LOGIN_URL')

class PageIncorrectLogin(unittest.TestCase):
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
    
    def test_incorrect_password(self):
        email = self.driver.find_element('id','email')
        email.send_keys(self.email)

        password = self.driver.find_element('id','pass')
        password.send_keys(self.password)

        login_button = self.driver.find_element('id','loginbutton')
        login_button.click()

        # Explicit wait
        wait = WebDriverWait(self.driver, 15)

        current_url = self.driver.current_url
        not_me_link_not_found = False

        try:
            self.driver.find_element(By.ID, "not_me_link")
        except NoSuchElementException:
            not_me_link_not_found = True

        if not_me_link_not_found or "login_attempt" in current_url or "/login" in current_url:
            self.assertTrue(True, "Login was unsuccessful.")
        else:
            self.assertTrue(False, "Login was successful.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    test_case = PageIncorrectLogin('test_incorrect_password', email, password, browser)
    unittest.main(argv=[''], exit=False)
