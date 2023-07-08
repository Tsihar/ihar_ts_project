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
    items_counter = "//span[@id='j-filter__counter']"
    paginator = "//div[@class='cr-paginator_page_list']"
    bomann_egg_cooker_price_number = "//span[@data-code='6608212']"
    bomann_egg_cooker_price_unit = "//span[@class='g-price__unit result__priceunit']"
    add_bomann_into_cart_button = "//*[@id='j-result-page-1']/li[4]/dl/div[2]/form/button"

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

    def get_items_counter(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.items_counter)))

    def get_paginator(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.paginator)))

    def get_bomann_egg_cooker_price_number(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.bomann_egg_cooker_price_number)))

    def get_bomann_egg_cooker_price_unit(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.bomann_egg_cooker_price_unit)))

    def get_add_bomann_into_cart_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.add_bomann_into_cart_button)))


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
        self.get_show_items_button().click()
        print('show items button is clicked')

    def paginator_text(self):
        paginator_text_value = self.get_paginator().text
        print(f'number of items to show is {paginator_text_value}')
        return paginator_text_value

    def paginator_items_quantity_on_page(self): #method to find the number of items in the list of filtered egg cookers
        splitted_paginator_text = self.paginator_text().split()
        items_quantity = splitted_paginator_text[3]
        print(f'number of items are displayed on the page is {items_quantity}')
        return items_quantity

    def full_bomann_price(self):
        first_price_value = self.get_bomann_egg_cooker_price_number().text
        second_price_value = self.get_bomann_egg_cooker_price_unit().text
        full_price_value = first_price_value + ' ' + second_price_value
        print(full_price_value)
        return full_price_value

    def click_add_bomann_into_cart_button(self):
        self.action.move_to_element(self.get_add_bomann_into_cart_button()).perform()
        self.get_add_bomann_into_cart_button().click()
        print('bomann egg cooker is added to the cart')

    """Methods"""

    def set_filters(self):
        self.set_min_price()
        self.set_max_price()
        self.click_checkbox_in_stock()
        self.click_dropdown_material()
        self.click_checkbox_material_plastic()
        self.click_show_items_button()


