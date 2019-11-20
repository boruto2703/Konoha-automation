import unittest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException

from src.common.TestBase import TestBase
from src.common.pages import ProjectPage
from src.common.locators import ProjectPageLocators, TeamPageLocators, \
    RepoPageLocators, CommonLocators, SettingsPageLocators
from src.common.errors import NotFoundError

with open('src/json/names.json', 'r') as namesfile:
    data = namesfile.read()
    names = json.loads(data)

with open('src/json/integrations.json', 'r') as authfile:
    data = authfile.read()
    integrations = json.loads(data)


class TestProjectListPage(TestBase):

    def setUp(self):
        self.main = ProjectPage(self.driver)
        try:
            current_url = self.driver.current_url
            if '/dashboard' not in current_url:
                self.main.login()
            current_url = self.driver.current_url
            self.main.find_element_with_wait({'by': By.ID, 'locator': 'txt-navbar-email'})
            if (current_url.endswith('/dashboard')
                    or current_url.endswith('/dashboard/')):
                # on Team page
                items = self.main.find_all_elements(TeamPageLocators.TEAM_LIST_ITEM)
                if len(items) == 0:
                    self.skipTest('Skip test because there\'s no teams')
                    print('Skip test because there\'s no teams')
                else:
                    items[0].click()
        except Exception:
            raise Exception('Cannot navigate to Test page')

    def test_TC_PP_001(self):
        """
        This test will test if the page is loaded successful
        """
        main = self.main

        # Check title
        main.assert_element_text(ProjectPageLocators.APPBAR_TEXT, 'Projects')

        # Calc number of projects in team
        main.find_element_with_wait(ProjectPageLocators.PROJECT_LIST)
        items = main.find_all_elements(ProjectPageLocators.PROJECT_ITEMS)
        print('Projects in team rendered')
        if len(items) == 0:
            print('Team has no projects')
        else:
            print(f'Team has {len(items)} project(s)')

        pass

    def test_TC_PP_002(self):
        """
        This test will test adding new project for admin user
        It will check if the project with name = names['new_project'] is
        already exist and will create if isn't
        """
        # This test will be skipped if the add btn is disabled
        # TODO Handle failed to create new proj, locators of swal
        main = self.main
        has_error = False
        try:
            found, idx = main.find_project_index_by_name(names['new_project'])
            if not found:
                main.create_new_project(self.skipTest, names['new_project'])

        except NoSuchElementException:
            has_error = True
            print(f'{self._testMethodName}: NoSuchElementException:'
                  ' Create new team page failed to load')
        except AssertionError:
            has_error = True
            print(f'{self._testMethodName}: AssertionError:'
                  ' New project\'s name displayed not correct')
        except Exception as e:
            has_error = True
            print(f'{self._testMethodName} Failed with {e}')

        if not has_error:
            print(f' % {self._testMethodName}: Success % ')

    def test_TC_PP_003(self):
        """
        This test will delete the project from the main project list page
        and delete the project created in test_TC_PP_002
        """
        self.main.find_and_delete_project(self.skipTest)

    def test_TC_PP_004(self):
        """
        This test will create and delete the project
        """
        main = self.main

        found, idx = main.find_project_index_by_name(names['new_project_004'])
        if found:
            project_item_locator = ProjectPageLocators.get_project_item_locator(idx + 1)
            main.click_with_delay(project_item_locator)
        else:
            main.create_new_project(self.skipTest, names['new_project_004'])
        main.click_with_delay(RepoPageLocators.DELETE_PROJECT_BTN, 15)
        main.click_if_posible(ProjectPageLocators.DELETE_PROJECT_POPUP_CONFIRM_BTN)
        main.click_if_posible(CommonLocators.SUCCESS_POPUP_BTN)
        print(f'Delete project with name {names["new_project_004"]} successfully')

    def test_TC_PP_005(self):
        """
        Open, edit and save project settings
        This test will run by following steps
        First: create new project name : "test_project_settings"
        Second: open settings
        Third: edit a settings
        Forth: save
        """
        main = self.main

        found, idx = main.find_project_index_by_name(names['project_for_test_0056_1'])
        if found:
            project_item_locator = ProjectPageLocators.get_project_item_locator(idx + 1)
            main.click_with_delay(project_item_locator)
        else:
            main.create_new_project(self.skipTest, names['project_for_test_0056_1'])

        main.click_with_delay(RepoPageLocators.PROJECT_SETTINGS_BTN, 15)
        main.click_with_delay(SettingsPageLocators.ANALYSIS_FIELD)
        main.input_to_field(SettingsPageLocators.EXCLUDE_FOLDER_INPUT_FIELD, 'doc')
        main.input_to_field(SettingsPageLocators.EXCLUDE_FOLDER_INPUT_FIELD, Keys.ENTER)
        main.click_with_delay(SettingsPageLocators.LANGUAGE_TO_ANALYSE_SELECT_FIELD)
        main.click_with_delay(SettingsPageLocators.get_selection_in_field(2))
        main.input_to_field(SettingsPageLocators.get_selection_in_field(2), Keys.ESCAPE)
        # main.click(SettingsPageLocators.ANALYSIS_FIELD)
        main.click_with_delay(SettingsPageLocators.INTEGRATIONS_FIELD)
        main.input_to_field(SettingsPageLocators.TFS_BASE_URI_INPUT_FIELD,
                            integrations['tfs_base_uri'], True)
        main.input_to_field(SettingsPageLocators.TFS_USERNAME_INPUT_FIELD,
                            integrations['tfs_username'], True)
        main.input_to_field(SettingsPageLocators.TFS_TOKEN_INPUT_FIELD,
                            integrations['tfs_token'], True)

        main.click_with_delay(SettingsPageLocators.SAVE_BTN, 20)
        try:
            main.click_if_posible(CommonLocators.SUCCESS_POPUP_BTN)
        except NotFoundError:
            main.click_if_posible(CommonLocators.ERROR_POPUP_BTN)
            raise Exception(f'Error when saving project settings')

    def test_TC_PP_006(self):
        """
        This test will check for 2 projects and will test the cloning settings function
        """
        main = self.main

        found_1, idx_1 = main.find_project_index_by_name(names['project_for_test_0056_1'])
        found_2, idx_2 = main.find_project_index_by_name(names['project_for_test_0056_2'])
        if not found_2:
            main.create_new_project(self.skipTest, names['project_for_test_0056_2'])
            main.click_with_delay(RepoPageLocators.GO_BACK_BTN)
        # copy
        main.click_with_delay(ProjectPageLocators.get_project_item_settings_btn_locator(idx_1))
        main.click_with_delay(ProjectPageLocators.COPY_SETTINGS_BTN)
        # paste
        main.click_with_delay(ProjectPageLocators.get_project_item_settings_btn_locator(idx_2))
        main.click_with_delay(ProjectPageLocators.PASTE_SETTINGS_BTN, 30)
        try:
            main.click_if_posible(CommonLocators.SUCCESS_POPUP_BTN)
        except NotFoundError:
            main.click_if_posible(CommonLocators.ERROR_POPUP_BTN)
            raise Exception(f'Error when saving project settings')
            # TODO: Delete project_for_test_0056_2

        self.main.find_and_delete_project(self.skipTest, names['project_for_test_0056_2'])


if __name__ == '__main__':
    unittest.main()
