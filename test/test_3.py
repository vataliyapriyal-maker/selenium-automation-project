from pages.attendance_request import attendance_req


def test_login(login_user):

    driver = login_user
    attendance_request = attendance_req(driver)

    attendance_request.click_req()
    attendance_request.click_attend()
    attendance_request.click_new()    
    attendance_request.enter_date("3/4/2026")
    attendance_request.clkintime("9:30 AM")
    attendance_request.clkout("6:30 PM")
    attendance_request.enter_reason("NA")
    attendance_request.save_details()
    
