from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.main_page import Main_page
from pages.manage_account_popup import Manage_account_popup


class Login_window(Base):

    # global email
    # email = "tita_13@mail.ru"

    def __init__(self, driver):
        super().__init__(driver)
        self.Manage_account_popup = Manage_account_popup
        self.Base = Base
        self.Main_page = Main_page
        self.driver = driver
        self.email = "tita_13@mail.ru"
        self.password = "0e24fd0b"

    """Locators"""

    email_input_field = "//input[@id='login-email']"
    password_input_field = "//input[@id='login-password']"
    login_submit_button = "//button[@data-testid='loginSubmit']"

    """Getters"""

    def get_email_input_field(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.email_input_field)))

    def get_password_input_field(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.password_input_field)))

    def get_login_submit_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.login_submit_button)))

    """Actions"""

    def insert_email(self, email):
        self.get_email_input_field().send_keys(email)
        print("email is inserted")

    def insert_password(self, password):
        self.get_password_input_field().send_keys(password)
        print("password is inserted")

    def click_login_submit_button(self):
        self.get_login_submit_button().click()
        print("Login submit button is clicked")

    """Methods"""

    def authorization(self):
        self.insert_email(self.email)
        self.insert_password(self.password)
        self.click_login_submit_button()
        self.Main_page.click_account_button()
        self.Base.assert_text(self.Manage_account_popup.get_email_word(), self.email)
