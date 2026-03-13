import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import login_page
import os
from datetime import datetime
from utilities.logger import logger
import pytest_html


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")

        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)
            print(f"\nScreenshot saved: {file_path}")

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://myclockview.com")
    assert  driver.title == "Myclockview-HRMS"  
    yield driver
    driver.quit()

@pytest.fixture    
def login_user(setup: WebDriver):

    driver = setup

    driver.get("https://myclockview.com")

    login = login_page(driver)

    login.login_click()
    logger.info("clicked login button")
    login.username("name@gmail.com")
    login.password_add("*****")
    login.done()

    
    return driver


    

