from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base



class Catalog_popup(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)

    """Locators"""

    kitchen_item = "//a[@href='/kitchen/']"
    show_all_button_cooking_appliances = "//*[@id='header']//div[3]/button"
    egg_cookers = "//a[@href='/egg_cookers/']"

    """Getters"""

    def get_kitchen_item(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.kitchen_item)))

    def get_show_all_c_a(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.show_all_button_cooking_appliances)))

    def get_egg_cookers(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.egg_cookers)))

    """Actions"""

    def expand_kitchen_items(self):
        self.action.move_to_element(self.get_kitchen_item()).perform()

    def expand_all_cooking_appliances(self):
        self.action.move_to_element(self.get_show_all_c_a()).perform()
        self.get_show_all_c_a().click()
        print('Egg cookers link is expanded')

    def click_egg_cookers(self):
        self.action.move_to_element(self.get_egg_cookers()).perform()
        self.get_egg_cookers().click()
        print('Egg cookers link is clicked')

    """Methods"""

    def open_egg_cookers_section(self):
        self.expand_kitchen_items()
        self.expand_all_cooking_appliances()
        self.click_egg_cookers()
