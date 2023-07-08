from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base



class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)

    """Locators"""

    first_price_part = "//div[@class='PriceBlock_priceBlock__3SERn']/span[1]"
    second_price_part = "//div[@class='PriceBlock_priceBlock__3SERn']//span[@class='PriceBlock_priceBlockEnd__16RaA']"
    order_button = "//div[@class='Button-module__buttonText']"
    remove_button = "//button[@aria-label='Удалить товар']"
    remove_confirmation_button = "//button[@data-testid='modal-confirmation-button']"

    """Getters"""

    def get_first_price_part(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.first_price_part)))

    def get_second_price_part(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.second_price_part)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    def get_remove_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.remove_button)))

    def get_remove_confirmation_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.remove_confirmation_button)))

    """Actions"""

    def full_price_in_cart(self):
        cart_first_price_value = self.get_first_price_part().text
        cart_second_price_value = self.get_second_price_part().text
        cart_full_price_value = cart_first_price_value + cart_second_price_value
        print(cart_full_price_value)
        return cart_full_price_value

    def click_order_button(self):
        self.get_order_button().click()
        print('Order button is clicked')

    def click_remove_button(self):
        self.get_remove_button().click()
        print('Remove button is clicked')

    def click_remove_confirmation_button(self):
        self.get_remove_confirmation_button().click()
        print('Removal is confirmed')

    """Methods"""

    def determine_order_details(self):
        self.click_order_button()
        self.assert_url('https://www.21vek.by/order/?step=delivery')
