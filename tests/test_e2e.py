import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from base.base_class import Base
from pages.cart_page import Cart_page
from pages.catalog_popup import Catalog_popup
from pages.egg_cookers_page import Egg_cookers_page
from pages.login_window import Login_window
from pages.main_page import Main_page
from pages.manage_account_popup import Manage_account_popup
from pages.order_details_page import Order_details_page


def test_e2e(open_site):

    fix_driver = open_site # pass driver using fixture "open_site"

    mp = Main_page(fix_driver)
    mp.open_manage_acc_popup()

    ap = Manage_account_popup(fix_driver)
    ap.open_login_window()

    lw = Login_window(fix_driver)
    lw.authorization()
    time.sleep(1) #fix of click account button before login verification

    # login verification
    mp.click_account_button()

    bc = Base(fix_driver)
    bc.assert_text(ap.get_email_word(), lw.email)

    # open catalog and choose section egg cookers
    mp.click_catalog_button()
    cp = Catalog_popup(fix_driver)
    cp.open_egg_cookers_section()

    ecp = Egg_cookers_page(fix_driver)
    bc.assert_text(ecp.get_egg_cookers_word(), ecp.egg_cookers)

    # set filters and verify that filter has been applied by comparing number of items in the paginator counter and "show items" button counter
    ecp.set_filters()
    bc.assert_text(ecp.get_items_counter(), ecp.paginator_items_quantity_on_page())

    #add egg cooker to cart and item verification
    cooker_price = ecp.full_bomann_price()
    ecp.click_add_bomann_into_cart_button()
    mp.click_cart_button()
    cart_p = Cart_page(fix_driver)
    bc.assertions(cooker_price, cart_p.full_price_in_cart())
    cart_p.determine_order_details()

    #verify item price in order details page
    odp = Order_details_page(fix_driver)
    bc.assertions(cooker_price, odp.full_price_in_order_details())
    odp.click_cross_button()






