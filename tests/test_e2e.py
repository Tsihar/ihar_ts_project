from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.main_page import Main_page


def test_e2e(open_site):
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # g = Service()
    # driver = webdriver.Chrome(options=options, service=g)
    fix_driver = open_site
    main = Main_page(fix_driver)
    main.authorization()
