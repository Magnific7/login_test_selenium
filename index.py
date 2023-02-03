import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
import environ

# environ.Env.read_env()
# environ.Env.read_env(env.str('ENV_PATH', '.env'))

LOGIN_URL=os.environ['LOGIN_URL']
print("LOGIN_URL",LOGIN_URL)

class FacebookLogin():
    def __init__(self, email, password, browser='Chrome',driver=None):
        # Store credentials for login
        self.email = email
        self.password = password
        if driver is None:
            driver={}
        else:
            self.driver = driver
            print(">>> driver",driver)
        if browser == 'Chrome':
            # Use chrome
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            # Set it to Firefox
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get(LOGIN_URL)
        time.sleep(1) 

    def login(self):

        email_element = self.driver.find_element_by_id('email')
        email_element.send_keys(self.email)
    
        password_element = self.driver.find_element_by_id('pass')
        password_element.send_keys(self.password) 
    
        login_button = self.driver.find_element_by_id('loginbutton')
        login_button.click() 
    
        time.sleep(2) 
        
if __name__ == '__main__':
    fb_login = FacebookLogin(email=os.environ['FB_EMAIL'], password=os.environ['FB_PASSWORD'], browser='chrome')
    fb_login.login()