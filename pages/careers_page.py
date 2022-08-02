from selenium.webdriver.common.by import By
from base.base_functions import BaseFunctions
from pages.team_page import TeamPage


class CareersPage(BaseFunctions):
    TEAMS_SECTION = (By.ID, "career-find-our-calling")
    LOCATIONS_SECTION = (By.ID, "career-our-location")
    LIFE_AT_INSIDER_SECTION = (By.CSS_SELECTOR, "[data-id='a8e7b90']")
    SEE_ALL_TEAMS_BUTTON = (By.CSS_SELECTOR, "#career-find-our-calling .btn")
    JOB_TITLES = (By.CSS_SELECTOR, ".job-title a h3")

    def __init__(self, driver):
        super().__init__(driver)

    def is_teams_section_visible(self):
        return self.is_element_displayed(self.TEAMS_SECTION)

    def is_locations_section_visible(self):
        return self.is_element_displayed(self.LOCATIONS_SECTION)

    def is_life_at_insider_section_visible(self):
        return self.is_element_displayed(self.LIFE_AT_INSIDER_SECTION)

    def click_see_all_teams(self):
        self.scroll_to_element(self.SEE_ALL_TEAMS_BUTTON)
        self.click_by(self.SEE_ALL_TEAMS_BUTTON)

    def get_team_page(self, team_name):
        team_element = self.get_element_with_text_in_list(self.JOB_TITLES, team_name)
        self.scroll_to_web_element(team_element)
        self.click_web_element(team_element)

        return TeamPage(self.driver)
