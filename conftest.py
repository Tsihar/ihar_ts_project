import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import Cart_page
from pages.main_page import Main_page


@pytest.fixture()
def open_site():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    url = 'https://www.21vek.by/'
    driver.get(url)
    driver.maximize_window()

    yield driver

    mp = Main_page(driver)
    mp.click_cart_button()
    cp = Cart_page(driver)
    cp.click_remove_button()
    cp.click_remove_confirmation_button()

    driver.quit()
