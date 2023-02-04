import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 

class FacebookLogin():
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
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@data-testid='left_nav_item_Me']")))
            profile_picture = self.driver.find_element("xpath","//a[@data-testid='left_nav_item_Me']")
            self.assertTrue(profile_picture.is_displayed())
            print("Login successful.")
            time.sleep(1)
        except TimeoutException:
            print("Login unsuccessful.")
            time.sleep(1)


if __name__ == '__main__':
    # try:
    fb_login = FacebookLogin(email=os.environ['FB_EMAIL'], password=os.environ['FB_PASSWORD'], browser=os.environ['BROWSER'])
    fb_login.login()
    # except Exception as e:
    #     print("Error:", e)
