import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 
import unittest
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException


load_dotenv()

email=os.getenv('INCORRECT_EMAIL')
password=os.getenv('FB_PASSWORD')
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

    def test_incorrect_login(self):
        email = self.driver.find_element(By.ID, 'email')
        email.send_keys(self.email)

        password = self.driver.find_element(By.ID, 'pass')
        password.send_keys(self.password)

        login_button = self.driver.find_element(By.ID, 'loginbutton')
        login_button.click()

        # Explicit wait
        wait = WebDriverWait(self.driver, 10)

        current_url = self.driver.current_url

        email_not_connected_not_found = False

        try:
            self.driver.find_element(By.CLASS_NAME, "_9ay7")
        except NoSuchElementException:
            email_not_connected_not_found = True

        if email_not_connected_not_found or "/login" in current_url:
            self.assertTrue(True, "Login was unsuccessful.")
        else:
            self.assertTrue(False, "Login was successful.")

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    test_case = PageIncorrectLogin('test_incorrect_login', email, password, browser)
    unittest.main(argv=[''], exit=False)
