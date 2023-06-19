from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super.__init__(driver)
        self.driver = driver

    """Locators"""

    account_button = "//button[@class='styles_userToolsToggler__imcSl']"

    """Getters"""

    def get_account_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.XPATH, self.account_button))

    """Actions"""

    def click_account_button(self):
        self.get_account_button().click()
        print('Account button is clicked')

    """Methods"""

    def open_login_menu(self):
        self.click_account_button()