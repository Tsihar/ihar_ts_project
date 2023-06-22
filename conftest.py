import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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

    # driver.quit()
