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
    price_slider = "//*[@id='j-filter__form']//div/a[1]"


    """Getters"""

    def get_egg_cookers_word(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.egg_cookers_text)))

    def get_price_slider(self):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.price_slider)))

    """Actions"""

    def set_min_price(self):
        self.action.click_and_hold(self.price_slider).move_by_offset(5, 0).release().perform()


