from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Egg_cookers_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)
        self.egg_cookers = "Яйцеварки"

    """Locators"""

    egg_cookers_text = "//h1[@class='content__header cr-category_header']"
    min_price = "//input[@name='filter[price][from]']"
    max_price = "//input[@name='filter[price][to]']"

    """Getters"""

    def get_egg_cookers_word(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.egg_cookers_text)))

    def get_min_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    """Actions"""

    def set_min_price(self):
        rn_min = self.generate_random_number(30, 35)
        self.get_min_price().send_keys(rn_min)
        print(f'min price is {rn_min}')

    def set_max_price(self):
        rn_max = self.generate_random_number(195, 200)
        self.get_max_price().send_keys(rn_max)
        print(f'max price is {rn_max}')

    """Methods"""

    def set_price_range(self):
        self.set_min_price()
        self.set_max_price()


