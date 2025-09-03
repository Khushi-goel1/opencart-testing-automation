from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.timeout = 10

    def open(self, url):
        self.browser.get(url)

    def find(self, locator):
        return WebDriverWait(self.browser, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        element = WebDriverWait(self.browser, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type(self, locator, text):
        field = self.find(locator)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def current_url(self):
        return self.browser.current_url
