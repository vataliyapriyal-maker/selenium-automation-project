from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.logger import logger


class attendance_req():

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)
        
        self.request = (By.XPATH,"//span[@class='nav-text' and text() = 'Leave Management']")
        self.attendance = (By.XPATH,"//span[@class='nav-text' and text() = 'Attendance Request']")
        self.new = (By.CLASS_NAME,"MuiButtonBase-root")
        self.date = (By.XPATH,"//input[@type='date']")
        self.clock_in_time = (By.ID,":r6:")
        self.clock_out_time = (By.ID,":r8:")
        self.reason = (By.NAME,"Reason")
        self.save = (By.XPATH,"//button[@type ='submit']")

    def click_req(self):
        try:
            click_request = self.wait.until(
                EC.element_to_be_clickable(self.request)
            ).click()
            logger.info("click on leave mangemnet sucessfully!")
        except:
            logger.error("failed to find request button") 

    def click_attend(self):
        try:    
            attend_click = self.wait.until(
                EC.element_to_be_clickable(self.attendance)
            ).click()
            time.sleep(5)

            logger.info("click on attendace request sucessfully!")
        except:
            logger.error("failed to find attendance request") 

    def click_new(self):
        try:
            apply_new = self.wait.until(
                EC.element_to_be_clickable(self.new)        
            ).click()

            logger.info("click on new sucessfully!")
        except:
            logger.error("failed to find new request button") 

    def enter_date(self,date):
        try:
            enter = self.wait.until(
                EC.element_to_be_clickable(self.date)
            )
            enter.send_keys(date)
            enter.send_keys(Keys.ENTER)

            logger.info(f"click on {date} sucessfully!")
        except:
            logger.error(f"failed to enter {date}") 

    def clkintime(self,time_value):
        try:
            clk_in_time = self.wait.until(
                EC.element_to_be_clickable(self.clock_in_time)
            )
            clk_in_time.send_keys(time_value)
            clk_in_time.send_keys(Keys.ENTER)
            logger.info(f"enter clockintime {time_value} sucessfully!")
        except:
            logger.error(f"failed to enter {time_value}") 

    def clkout(self ,time_value):
        try:
            clk_out_time = self.wait.until(
                EC.element_to_be_clickable(self.clock_out_time)
            )
            clk_out_time.send_keys(time_value)
            clk_out_time.send_keys(Keys.ENTER)

            logger.info(f"enter clockout {time_value} sucessfully!")
        except:
            logger.error(f"failed to enter {time_value}") 
        

    def enter_reason(self,reason):
        try:
            reason_enter = self.wait.until(
                EC.element_to_be_clickable(self.reason)
            )
            reason_enter.send_keys(reason)

            logger.info(f"enter reason {reason} sucessfully!")
        except:
            logger.error(f"failed to enter {reason}") 

    def save_details(self):
        try:
            s_ave = self.wait.until(
                EC.element_to_be_clickable(self.save)
            ).click()

            logger.info("save sucessfully!")
            time.sleep(2) 
        except:
            logger.error("failed to save attendence request")
        



            


