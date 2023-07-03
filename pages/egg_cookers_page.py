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
    checkbox_in_stock = "//*[@id='j-filter__form']/div[2]/dl/div/dd[1]/label"
    dropdown_material = "//*[@id='j-filter__form']/div[4]/dl[3]/dt/span"
    checkbox_material_plastic = "//*[@id='j-filter__form']/div[4]/dl[3]/div/dd[1]/label"
    show_items_button = "//span[@class='g-button__text']"

    """Getters"""

    def get_egg_cookers_word(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.egg_cookers_text)))

    def get_min_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_checkbox_in_stock(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_in_stock)))

    def get_dropdown_material(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_material)))

    def get_checkbox_material_plastic(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_material_plastic)))

    def get_show_items_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.show_items_button)))


    """Actions"""

    def set_min_price(self):
        rn_min = self.generate_random_number(30, 35)
        self.get_min_price().send_keys(rn_min)
        print(f'min price is {rn_min}')

    def set_max_price(self):
        rn_max = self.generate_random_number(195, 200)
        self.get_max_price().send_keys(rn_max)
        print(f'max price is {rn_max}')

    def click_checkbox_in_stock(self):
        self.get_checkbox_in_stock().click()

    def click_dropdown_material(self):
        self.get_dropdown_material().click()

    def click_checkbox_material_plastic(self):
        self.get_checkbox_material_plastic().click()

    def click_show_items_button(self):
        self.get_show_items_button()


    """Methods"""

    def set_filters(self):
        self.set_min_price()
        self.set_max_price()
        self.click_checkbox_in_stock()
        self.click_dropdown_material()
        self.click_checkbox_material_plastic()
        self.click_show_items_button()


