from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class InventoryPage(BasePage):
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BACKPACK_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CSS_SELECTOR, "a.shopping_cart_link span.shopping_cart_badge")

    def add_backpack_to_cart(self):
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(self.BACKPACK_ADD_BUTTON)
        ).click()

        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.BACKPACK_REMOVE_BUTTON)
        )

    def get_cart_count(self):
        try:
            badge = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(self.CART_BADGE)
            )
            return badge.text
        except TimeoutException:
            return None
