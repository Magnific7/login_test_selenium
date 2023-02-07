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

email=os.getenv('BLOCKED_EMAIL')
password=os.getenv('BLOCKED_ACCOUNT_PASSWORD')
browser=os.getenv('BROWSER')
LOGIN_URL = os.getenv('LOGIN_URL')


class BlockedAccountLogin(unittest.TestCase):
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

    def test_blocked_account_login(self):
        email = self.driver.find_element(By.ID, 'email')
        email.send_keys(self.email)

        password = self.driver.find_element(By.ID, 'pass')
        password.send_keys(self.password)

        login_button = self.driver.find_element(By.ID, 'loginbutton')
        login_button.click()

        # Explicit wait
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_changes(self.driver.current_url))
        current_url = self.driver.current_url

        if "/disabled" in current_url:
            self.assertTrue(True, "Account has been disabled")
        else:
            self.assertTrue(False, "Account is active ")

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    test_case = BlockedAccountLogin('test_blocked_account_login', email, password, browser)
    unittest.main(argv=[''], exit=False)


# x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x14z4hjw x3x7a5m xngnso2 x1qb5hxa x1xlr1w8 xzsf02u x1yc453h