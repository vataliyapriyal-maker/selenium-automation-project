from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.logger import logger

class Logout():

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)

        self.profile = (By.CLASS_NAME,"userdata")
        self.log_out = (By.CLASS_NAME,"logout-button")

    def clk_profile(self):
        try:    
            self.wait.until(
                EC.element_to_be_clickable(self.profile)
            ).click()
            logger.info("clicked profile!")
            time.sleep(3)

        except:

            logger.error("error occured!")    
            time.sleep(3) 

    def clk_logout(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.log_out)
            ).click()
            logger.info("logout sucessful!!")
            time.sleep(5)

        except:

            logger.error("error occured!")
            time.sleep(2)    
