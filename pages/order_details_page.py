from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base



class Order_details_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)

    """Locators"""

    first_price_part_ordered = "//div[@data-testid='footer-price']/span[1]"
    second_price_part_ordered = "//div[@data-testid='footer-price']/span[2]"
    cross_button = "//button[@data-testid='header-close-button']"

    """Getters"""

    def get_first_price_part_ordered(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.first_price_part_ordered)))

    def get_second_price_part_ordered(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.second_price_part_ordered)))

    def get_cross_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.cross_button)))

    """Actions"""

    def full_price_in_order_details(self):
        cart_first_price_value_ordered = self.get_first_price_part_ordered().text
        cart_second_price_value_ordered = self.get_second_price_part_ordered().text
        cart_full_price_value_ordered = cart_first_price_value_ordered + cart_second_price_value_ordered
        print(cart_full_price_value_ordered)
        return cart_full_price_value_ordered

    def click_cross_button(self):
        self.get_cross_button().click()
        print('Cross button is clicked')

    """Methods"""
