from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = 'https://www.21vek.by/'

    """Locators"""

    ok_cookies_button = "//button[@class='Button-module__button Button-module__blue-primary']"
    account_button = "//button[@class='styles_userToolsToggler__imcSl']"

    """Getters"""

    def get_ok_cookies_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.ok_cookies_button)))

    def get_account_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.account_button)))

    """Actions"""

    def click_ok_cookies_button(self):
        self.get_ok_cookies_button().click()
        print('Ok cookies button is clicked')

    def click_account_button(self):
        self.get_account_button().click()
        print('Account button is clicked')

    """Methods"""

    def open_manage_acc_popup(self):
        self.click_ok_cookies_button()  # accept cookies
        self.click_account_button()
