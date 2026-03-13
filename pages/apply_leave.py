from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.logger import logger

class apply_new_leave():

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver ,10)
        
        self.request = (By.XPATH,"//span[@class='nav-text' and text() = 'Leave Management']")
        self.leave = (By.CSS_SELECTOR, "a[href='/applyleave']")
        self.apply = (By.CLASS_NAME,"btn-primary-action")
        self.name = (By.XPATH,"//div[@id ='employeename']//input[@role = 'combobox']")
        self.type = (By.XPATH,"//div[@id ='leaveType']//input[@role = 'combobox']")
        self.l_date = (By.NAME,"date")
        self.full_day =(By.XPATH,"//div[@id = 'dayTypeName_0']//input[@role = 'combobox']")
        self.l_reason = (By.NAME,"leavereason")
        self.l_add = (By.CLASS_NAME,"btn")

    def click_req(self):
        try:
            click_request = self.wait.until(
                EC.element_to_be_clickable(self.request)
            ).click()

            logger.info("click on leave mangement sucessfullly!!")

        except:

            logger.error("failed to find leave management button")    

    def clk_leave(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.leave)
            ).click()

            logger.info("click on apply leave sucessfully!")

        except:

            logger.error("failed to find apply leave button") 

    def l_apply(self):
        try:
            apply_leave = self.wait.until(
                EC.element_to_be_clickable(self.apply)
            ).click()

            logger.info("click on +apply sucessfully!")

        except:

            logger.error("failed to find supply button")


    def emp_name(self,name):
       try:
            type_leave = self.wait.until(
                    EC.element_to_be_clickable(self.name)
                )
            type_leave.send_keys(name)
            type_leave.send_keys(Keys.ENTER)

            logger.info(f"enter name : {name} sucessfully!")

       except:
            
            logger.error(f"failed to enter name: {name}") 


    def l_type(self,l_Type):
       try:
        type_leave = self.wait.until(
                EC.element_to_be_clickable(self.type)
            )
        type_leave.clear()
        type_leave.send_keys(l_Type)
        type_leave.send_keys(Keys.ENTER)
        time.sleep(4)
        logger.info(f"enter type of leave : {l_Type} sucessfully!")

       except Exception as e:
            logger.error(f"Failed to enter leave type. Error: {str(e)}") 
            raise 

    # def emp_name(self,name):
    #    try:
    #         type_leave = self.wait.until(
    #                 EC.element_to_be_clickable(self.name)
    #             )
    #         type_leave.send_keys(name)
    #         type_leave.send_keys(Keys.ENTER)

    #         logger.info(f"enter name : {name} sucessfully!")

    #    except:
            
    #         logger.error(f"failed to enter name: {name}") 

    def leave_date(self,date):
        try:

            date_leave = self.wait.until(
                EC.element_to_be_clickable(self.l_date)
            )
            date_leave.send_keys(date)
            date_leave.send_keys(Keys.ENTER)

            logger.info(f"enter Date {date} sucessfully!")

        except:

            logger.error(f"failed to enter date : {date}") 

    def f_day(self,full_day):
        try:
            day = self.wait.until(
                EC.element_to_be_clickable(self.full_day)
            )
            day.send_keys(full_day)
            day.send_keys(Keys.ENTER)

            logger.info(f"select {full_day} sucessfully!") 

        except:

            logger.error(f"failed to select {full_day}")     


    def leave_reason(self,reason):
        try:
            reason_leave = self.wait.until(
                EC.element_to_be_clickable(self.l_reason)
            )
            reason_leave.send_keys(reason)
            reason_leave.send_keys(Keys.ENTER)

            logger.info(f"enter reason {reason} sucessfully!")

        except:

            logger.error(f"failed to enter {reason} ") 


    def add_leave(self):
        try:
            add_l = self.wait.until(
                EC.element_to_be_clickable(self.l_add)
            ).click()
            logger.info("apply leave sucessfully!")

        except:
            logger.error("failed to apply leave!")
            time.sleep(6)














