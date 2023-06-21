from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.main_page import Main_page


def test_e2e():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    main = Main_page(driver)
    main.authorization()
