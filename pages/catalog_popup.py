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

    tourism_item = "//span[@class='styles_categoryName__28yR1 styles_categoryName__ZUtLQ']"

    """Getters"""

    def get_tourism_item(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.tourism_item)))

    """Actions"""

    def expand_tourism_items(self):
        self.action.move_to_element(self.get_tourism_item()).perform()

    """Methods"""