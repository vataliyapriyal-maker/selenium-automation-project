from pages.login_page import login_page
from pages.homepage import home_page
from pages.attendance_request import attendance_req
from pages.apply_leave import apply_new_leave


def test_login(login_user):

    driver = login_user
    homepage = home_page(driver)

    homepage.clck_clockin()