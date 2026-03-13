from pages.apply_leave import apply_new_leave


def test_login(login_user):

    driver = login_user
    apply_leave = apply_new_leave(driver)

    apply_leave.click_req()
    apply_leave.clk_leave()
    apply_leave.l_apply()
    apply_leave.emp_name("piyu Patel")
    apply_leave.l_type(" Sick Leave (SL)")
    apply_leave.leave_date("18/03/2026")
    apply_leave.f_day("Full Day")
    apply_leave.leave_reason("stomach pain")
    apply_leave.add_leave()
