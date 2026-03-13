
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.logger import logger

class login_page():

    def __init__(self , driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

        self.login = (By.LINK_TEXT,"Login")
        self.email = (By.CLASS_NAME,"form-control")
        self.password = (By.XPATH,"//input[contains(@type,'password')]")
        self.submit = (By.XPATH,"//button[@type='submit']")  

    def login_click(self):
        try:
            login_button = self.wait.until(
                EC.element_to_be_clickable(self.login)
            ).click()
            logger.info("clicked login button")
        except:
            logger.error("failed to find login button")    

    def username(self,email):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.email)
            ).send_keys(email)
            logger.info(f"Enter Emailid : {email}")
        except:
            logger.error(f"failed to enter {email}") 

    def password_add(self,password):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.password)
            ).send_keys(password)
            logger.info(f"enter password : {password}")
        except:
            logger.error(f"failed to enter {password}")     

    def done(self):
        try:
            sub = self.wait.until(
                EC.element_to_be_clickable(self.submit)
            ).click() 
            logger.info("clicked login button")
        except:
            logger.error("failed to login ")  
        time.sleep(3)

