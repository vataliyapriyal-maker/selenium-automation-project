from pages.Logout_page import Logout
from pages.login_page import login_page

def test_logout(login_user):

    driver = login_user
    Logout_page = Logout(driver)

    Logout_page.clk_profile()
    Logout_page.clk_logout()