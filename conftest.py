import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def set_up():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    driver.maximize_window()
    url = 'https://www.21vek.by/'
    driver.get(url)
    #
    # yield
    #
    # driver.quit()
