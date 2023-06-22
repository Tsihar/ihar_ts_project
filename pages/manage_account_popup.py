from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Manage_account_popup(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    enter_word = "//h5[@class='style_formTitle__hRNRz']"
    login_button = "//button[@data-testid='loginButton']"
    email_word = "//span[@class='userToolsSubtitle']"

    """Getters"""

    def get_login_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_email_word(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.email_word)))

    """Actions"""

    def click_login_button(self):
        self.get_login_button().click()
        print('Login button is clicked')

    def get_enter_word(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.enter_word)))

    """Methods"""

    def open_login_window(self):
        self.click_login_button()
        self.assert_text(self.get_enter_word(), "Вход")
