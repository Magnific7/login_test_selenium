import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time 

class FacebookIncorrectLogin(unittest.TestCase):
    def __init__(self, email, password, browser='Chrome', driver=None):
    # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Chrome':
                self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
                self.driver = webdriver.Firefox()
        self.driver.get(os.environ['LOGIN_URL'])
        time.sleep(1)


        time.sleep(2) 

    def test_incorrect_login(self):
        email = self.driver.find_element('id','email')
        email.send_keys("incorrect_email@example.com")

        password = self.driver.find_element('id','pass')
        password.send_keys("incorrect_password")

        login_button = self.driver.find_element('id','loginbutton')
        login_button.click()

        current_url = self.driver.current_url
        if "facebook.com/login" in current_url:
            self.assertTrue(True, "Login was unsuccessful.")
            print("Login was unsuccessful.")
        else:
            self.assertTrue(False, "Login was successful.")
            print("Login was successful.")
            
if __name__ == '__main__':
    try:
        fb_login = FacebookIncorrectLogin(email='dummy@gmail.com', password=os.environ['FB_PASSWORD'], browser=os.environ['BROWSER'])
        fb_login.test_incorrect_login()
    except Exception as e:
        print("Error:", e)
