from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_window import Login_window
from pages.main_page import Main_page
from pages.manage_account_popup import Manage_account_popup


def test_e2e(open_site):

    fix_driver = open_site # pass driver using fixture "open_site"

    mp = Main_page(fix_driver)
    mp.open_manage_acc_popup()

    uap = Manage_account_popup(fix_driver)
    uap.open_login_window()

    lw = Login_window(fix_driver)
    lw.authorization()

