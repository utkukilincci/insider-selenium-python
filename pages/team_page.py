from selenium.webdriver.common.by import By
from base.base_functions import BaseFunctions
from pages.positions_page import PositionsPage


class TeamPage(BaseFunctions):
    SEE_ALL_JOBS_BUTTON = (By.CSS_SELECTOR, ".flex-column .button-group .btn")
    NAVIGATION_BAR_MENUS = (By.ID, "mega-menu-1")

    def __init__(self, driver):
        super().__init__(driver)

    def get_all_jobs(self):
        self.click_by(self.SEE_ALL_JOBS_BUTTON)
        self.wait_for_clickable_element(self.NAVIGATION_BAR_MENUS)

        return PositionsPage(self.driver)
