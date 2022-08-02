from selenium.webdriver.common.by import By
from base.base_functions import BaseFunctions
from pages.careers_page import CareersPage


class HomePage(BaseFunctions):
    NAVIGATION_BAR_MENUS = (By.ID, "mega-menu-1")
    FLEX_SECTIONS_IN_DROPDOWN_MENUS = (By.CSS_SELECTOR, ".dropdown-item .flex-row a h5")
    ACCEPT_COOKIES = (By.ID, "wt-cli-accept-all-btn")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_home_page(self):
        self.navigate_url("https://useinsider.com")
        self.click_by(self.ACCEPT_COOKIES)

    def click_menu_in_navigation_bar(self, menu_name):
        menu = self.get_element_with_text_in_list(self.NAVIGATION_BAR_MENUS, menu_name)
        self.click_web_element(menu)

    def click_sub_item_in_dropdown_menu(self, section_name):
        flex_section = self.get_element_with_text_in_list(self.FLEX_SECTIONS_IN_DROPDOWN_MENUS, section_name)
        self.click_web_element(flex_section)

        return CareersPage(self.driver)
