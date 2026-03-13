from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.logger import logger

class expense():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,15)


        self.request = (By.XPATH,"//span[@class='nav-text' and text() = 'Leave Management']")
        self.click_expense =(By.CSS_SELECTOR,"a[href = '/expense']")
        self.add_new = (By.XPATH,"//button[@type = 'button']")
        self.ex_date = (By.NAME,"date")
        self.ex_name = (By.NAME,"category")
        self.ex_amount = (By.NAME,"amount")
        self.ex_note = (By.XPATH,"//textarea[@placeholder = 'Enter note']")
        self.ex_save = (By.XPATH,"//button[@type='submit']")
        self.work = (By.XPATH,"//span[@class = 'arrow-icon']")
        self.dash = (By.XPATH, "//a[@href='/mywork' and contains(@class,'submenu-item')]")
        self.clock_out = (By.XPATH,"//button[@type='button' and contains(text(),'Clockout')]")

    def click_req(self):
        try:

            click_request = self.wait.until(
                EC.element_to_be_clickable(self.request)
            ).click()
            logger.info("click on leave management sucessfully!")  

        except:

            logger.error("failed to find leave management ") 



    def expenses_clk(self):
        try:

            self.wait.until(
                EC.element_to_be_clickable(self.click_expense)
            ).click()
            logger.info("click on expense sucessfully!") 

        except:

            logger.error("failed to click on expense button! ") 


    def add_expenses(self):
        try:

            self.wait.until(
                EC.element_to_be_clickable(self.add_new)
            ).click()
            logger.info("click on new expense sucessfully!")  

        except:

            logger.error("failed to click on new button")    


    def expense_date(self,date):
        try:

            self.wait.until(
                EC.element_to_be_clickable(self.ex_date)
            ).send_keys(date)

            logger.info(f"enter date of expenses : {date} sucessfully!") 

        except:

            logger.error(f"failed to enter date : {date}")    

    def expenses_name(self,name):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.ex_name)
            ).send_keys(name)

            logger.info(f"enter expense name {name} sucessfully!")

        except:

            logger.error(f"failed to enter name : {name} ")        


    def expenses_amount(self,amount):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.ex_amount)
            ).send_keys(amount)

            logger.info(f"enter amount {amount} sucessfully!") 

        except:

            logger.error(f"failed to enter amount : {amount}")  


    def expenses_note(self,note):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.ex_note)
            ).send_keys(note) 

            logger.info(f"enter note {note} sucessfully!")

        except:

            logger.error(f"faileed to enter note : {note} ")  


    def save_expense(self):
        try:

            self.wait.until(
                EC.element_to_be_clickable(self.ex_save)
            ).click()

            logger.info("expense save sucessfully! ")

        except:

            logger.error("failed to save expense") 

        time.sleep(4)

    def manage_work(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.work)
            ).click() 
            time.sleep(2) 

            logger.info("click on manage work sucessfully!") 

        except:

            logger.error("failed to click on manage work button") 

    def dash_board(self):
        try:

            self.wait.until(
                EC.element_to_be_clickable(self.dash)
            ).click()  

            logger.info("click on dashboard sucessfully!") 

        except:

            logger.error("failed to click on dashboard")    

    def clk_out(self):
        try:

            self.wait.until(
                EC.element_to_be_clickable(self.clock_out)
            ).click()

            logger.info("clockout sucessfully!")
            time.sleep(5)

        except:

            logger.error(" failed to clock out! ")
            time.sleep(3)






