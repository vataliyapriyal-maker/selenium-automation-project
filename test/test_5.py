from pages.Expenses import expense


def test_login(login_user):

    driver = login_user
    Expenses = expense(driver)
    
    Expenses.click_req()
    Expenses.expenses_clk()
    Expenses.add_expenses()
    Expenses.expense_date("4/03/2026")
    Expenses.expenses_name("Laptop display repairing")
    Expenses.expenses_amount("6000")
    Expenses.expenses_note("NA")
    Expenses.save_expense()
    Expenses.manage_work()
    Expenses.dash_board()
    Expenses.clk_out()
