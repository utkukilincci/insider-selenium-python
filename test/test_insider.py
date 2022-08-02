import unittest
import pytest
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestInsider(unittest.TestCase):

    def test_insider(self):
        nav_menu_name = "More"
        nav_sub_item_name = "Careers"
        department_name = "Quality Assurance"
        location = "Istanbul, Turkey"

        home_page = HomePage(self.driver)
        home_page.navigate_home_page()

        home_page.click_menu_in_navigation_bar(nav_menu_name)
        careers_page = home_page.click_sub_item_in_dropdown_menu(nav_sub_item_name)

        self.assertTrue(
            careers_page.is_teams_section_visible(), "Teams Section is not visible"
        )
        self.assertTrue(
            careers_page.is_locations_section_visible(), "Locations Section is not visible"
        )
        self.assertTrue(
            careers_page.is_life_at_insider_section_visible(), "Life at Insider section is not visible"
        )

        careers_page.click_see_all_teams()
        team_page = careers_page.get_team_page(department_name)
        position_page = team_page.get_all_jobs()
        position_page.set_location_filter(location)

        self.assertTrue(
            position_page.is_there_any_position(), "There is no position"
        )
        self.assertTrue(
            position_page.is_positions_department_true(department_name), "Positions Department name is incorrect"
        )
        self.assertTrue(
            position_page.is_positions_location_true(location), "Positions Location is incorrect"
        )
        self.assertTrue(
            position_page.is_positions_has_apply_button(), "Positions has no apply button"
        )

        lever_page = position_page.click_apply_button_for_first_position()
        lever_page.switch_tab()

        self.assertTrue(
            lever_page.is_lever_page_opened(), "Lever page is not opened"
        )
