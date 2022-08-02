from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseFunctions:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(driver, 30)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})", element)
        sleep(1)

    def scroll_to_web_element(self, web_element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})", web_element)
        sleep(1)

    def wait_for_clickable_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def click_by(self, locator):
        element = self.find_element(locator)
        element.click()

    def click_web_element(self, web_element):
        web_element.click()

    def navigate_url(self, url):
        self.driver.get(url)

    def is_element_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def get_element_with_text_in_list(self, locator, text):
        sleep(1)
        element_list = self.get_elements(locator)

        for element in element_list:
            if element.text == text:
                return element

        print("\nelement yok")

    def get_element_text(self, locator):
        text = self.find_element(locator).text

        return text

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_web_elements(self, web_element):
        return self.driver.find_elements(*web_element)

    def get_sub_element(self, web_element, locator):
        return web_element.find_element(*locator)

    def get_sub_elements(self, web_element, locator):
        return web_element.find_elements(*locator)

    def switch_tab(self):
        sleep(3)
        self.wait.until(EC.number_of_windows_to_be(2))
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    def get_url(self):
        return self.driver.current_url

    def take_screenshot(self, name):
        self.driver.save_screenshot("screenshots/" + name + "123.png")

