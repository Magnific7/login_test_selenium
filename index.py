import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time 

LOGIN_URL='https://www.facebook.com/login.php'
print("LOGIN_URL",LOGIN_URL)

class FacebookLogin():
    def __init__(self, email, password, browser='Chrome', driver=None):
    # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Chrome':
                self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
                self.driver = webdriver.Firefox()
        self.driver.get(LOGIN_URL)
        time.sleep(1)

 

    def login(self):
        email_element = self.driver.find_element('id','email')
        email_element.send_keys(self.email)
    
        password_element = self.driver.find_element('id','pass')
        password_element.send_keys(self.password) 
    
        login_button = self.driver.find_element('id','loginbutton')
        login_button.click() 

        time.sleep(2) 
        
if __name__ == '__main__':
    try:
        fb_login = FacebookLogin(email=os.environ['FB_EMAIL'], password=os.environ['FB_PASSWORD'], browser=os.environ['BROWSER'])
        fb_login.login()
    except Exception as e:
        print("Error:", e)
