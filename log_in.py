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


class FacebookLogin(unittest.TestCase):
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

 

    def login(self):
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
            print("Login was successful.")
        else:
            self.assertTrue(False, "Login was unsuccessful.")
            print("Login was unsuccessful.")

if __name__ == '__main__':
    try:
        fb_login = FacebookLogin(email=os.environ['FB_EMAIL'], password=os.environ['FB_PASSWORD'], browser=os.environ['BROWSER'])
        fb_login.login()
    except Exception as e:
        print("Error:", e)
