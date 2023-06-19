from pages.main_page import Main_page

def test_e2e(set_up_webdriver):

    main = Main_page(driver)
    main.open_login_menu()