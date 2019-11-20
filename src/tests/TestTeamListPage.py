import unittest
import json

from selenium.webdriver.common.by import By
from src.common.TestBase import TestBase
from src.common.pages import TeamPage
from src.common.locators import TeamPageLocators
with open('src/json/names.json', 'r') as namesfile:
    data = namesfile.read()
names = json.loads(data)


class TestTeamListPage(TestBase):

    def setUp(self):
        self.main = TeamPage(self.driver)
        try:
            current_url = self.driver.current_url
            if '/dashboard' not in current_url:
                self.main.login()
            current_url = self.driver.current_url

            self.main.find_element_with_wait({'by': By.ID, 'locator': 'txt-navbar-email'})
            print('\nStart new test in Team Page')
            on_team_page = False
            if (current_url.endswith('/dashboard')
                    or current_url.endswith('/dashboard/')):
                on_team_page = True
            if on_team_page is False:
                print('\nSkip Test because we are not in Team List Page')
                self.skipTest('We are not in Team List page')
        except Exception as e:
            print(f'Test cannot run because of error: {e}')
            raise Exception('Cannot navigate to Team list page')

    def test_TC_TP_001(self):
        """
        Load teams list page
        By: Find the element after login
        Check the breadcrums text
        Check from the toolbar
        """
        main = self.main

        # Check if logged and no internal server error
        main.find_element_with_wait({'by': By.ID, 'locator': 'txt-navbar-email'})
        print(f'{self._testMethodName}: Page loaded without internal server error')

        # 3rd, check for the team item
        self.driver.find_element(By.ID, 'ins-tour-team-list')
        items = self.driver.find_elements(TeamPageLocators.TEAM_LIST_ITEM['by'],
                                          TeamPageLocators.TEAM_LIST_ITEM['locator'])
        if len(items) == 0:
            print('No teams available')
        else:
            print(f'Team items loaded: {len(items)} teams')

        pass

    def test_TC_TP_002(self):
        """
        Add new team for superuser
        """
        self.main.click_if_posible({'by': By.ID, 'locator': 'btn-add-new-team'})
        self.main.input_to_field(TeamPageLocators.ADD_NEW_TEAM_FORM_FIELD, names['new_team'])
        self.main.click_with_delay(TeamPageLocators.ADD_NEW_TEAM_FORM_BTN)
        print(f'{self._testMethodName}: Create new team successfully')


if __name__ == '__main__':
    unittest.main()
