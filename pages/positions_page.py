from time import sleep

from selenium.webdriver.common.by import By
from base.base_functions import BaseFunctions
from pages.lever_page import LeverPage


class PositionsPage(BaseFunctions):
    LOCATION_FILTER = (By.ID, "select2-filter-by-location-container")
    LOCATION_SELECTION = (By.XPATH, "//*[@class='select2-results__option'][text()='{}']")
    POSITIONS = (By.CSS_SELECTOR, '.position-list-item')
    POSITIONS_DEPARTMENT = (By.CSS_SELECTOR, '.position-department')
    POSITIONS_LOCATION = (By.CSS_SELECTOR, '.position-location')
    GENERIC_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn")

    def __init__(self, driver):
        super().__init__(driver)

    def set_location_filter(self, location):
        self.click_by(self.LOCATION_FILTER)
        location_element = list(self.LOCATION_SELECTION)
        location_element[1] = self.LOCATION_SELECTION[1].format(location)
        self.LOCATION_SELECTION = tuple(location_element)
        self.scroll_to_element(self.LOCATION_SELECTION)
        self.click_by(self.LOCATION_SELECTION)
        sleep(2)

    def is_there_any_position(self):
        positions = self.get_elements(self.POSITIONS)

        return len(positions) > 0

    def is_positions_department_true(self, expected_name):
        position_list = self.get_elements(self.POSITIONS_DEPARTMENT)

        for position in position_list:
            is_text_true = position.text == expected_name
            if is_text_true is False:
                return False

        return True

    def is_positions_location_true(self, expected_name):
        position_list = self.get_elements(self.POSITIONS_LOCATION)

        for position in position_list:
            is_text_true = position.text == expected_name
            if is_text_true is False:
                return False

        return True

    def is_positions_has_apply_button(self):
        positions = self.get_elements(self.POSITIONS)

        for position in positions:
            apply_button = self.get_sub_elements(position, self.GENERIC_BUTTON_LOCATOR)
            if len(apply_button) < 1:
                return False

        return True

    def click_apply_button_for_first_position(self):
        positions = self.get_elements(self.POSITIONS)
        apply_button = self.get_sub_element(positions[0], self.GENERIC_BUTTON_LOCATOR)
        self.scroll_to_web_element(apply_button)
        self.click_web_element(apply_button)

        return LeverPage(self.driver)
