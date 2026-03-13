from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.logger import logger

class home_page():

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)

        self.clock_in = (By.XPATH,"//button[@type='button']")

    def clck_clockin(self):
        clock_in_click = self.wait.until(
            EC.element_to_be_clickable(self.clock_in)
        ).click()
        try:
            logger.info("clockin sucessfully!")
        except:
            logger.error()    
        time.sleep(5)
        