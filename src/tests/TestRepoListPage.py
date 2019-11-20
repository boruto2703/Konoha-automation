import unittest
import json

from selenium.webdriver.common.by import By
from src.common.TestBase import TestBase
from src.common.pages import RepoPage
from src.common.locators import RepoPageLocators, \
    ProjectPageLocators, CommonLocators, TeamPageLocators


with open('src/json/names.json', 'r') as namesfile:
    data = namesfile.read()
names = json.loads(data)


class TestRepoListPage(TestBase):

    def setUp(self):
        """
        Setup test for repo list page:
        - login
        - Go to team page -> project page -> repo page
        """
        self.main = RepoPage(self.driver)
        try:
            current_url = self.driver.current_url
            if '/dashboard' not in current_url:
                self.main.login()
            self.main.find_element_with_wait({'by': By.ID, 'locator': 'txt-navbar-email'})
            current_url = self.driver.current_url

            if (current_url.endswith('/dashboard')
                    or current_url.endswith('/dashboard/')):
                # on Team page
                items = self.main.find_all_elements(TeamPageLocators.TEAM_LIST_ITEM)
                if len(items) == 0:
                    self.skipTest('Skip test because there\'s no teams')
                    print('Skip test because there\'s no teams')
                else:
                    items[0].click()
                    # on project page
                    found, project_idx = self.main.find_project_index_by_name(
                        names['project_for_test_0056_1'])
                    if not found:
                        self.main.create_new_project(
                            self.skipTest, names['project_for_test_0056_1'])
                    else:
                        project_item_locator = ProjectPageLocators.get_project_item_locator(
                            project_idx + 1)
                        self.main.click_with_delay(project_item_locator)

            if self._testMethodName == 'test_TC_RP_008':
                pass
            else:
                can_add_repo = self.main.check_element_enable_by_locator(
                    RepoPageLocators.ADD_REPO_MENU_BTN, 15)
                if can_add_repo is False:
                    print(f'{self._testMethodName} skipped: user cannot add repo')
                    self.skipTest(f'Test {self._testMethodName} skipped: user cannot add repo')

        except Exception:
            raise Exception('Cannot navigate to Repositories Page')

    def test_TC_RP_001(self):
        """
        Test with adding repos from github
        First check if the page is showing the add token button (need to add token)
        or list of repos (had token)
        Then if need to add token, click button and going with the username and password
        from auth.json file (failed if missing data)
        If token has already added, choose 2 last repos and then delete the first chip
        Finally click on the add button, and check the success popup showed
        """
        main = self.main
        main.click_with_delay(RepoPageLocators.ADD_REPO_MENU_BTN)
        main.click_with_delay(RepoPageLocators.get_add_repo_service_btn_locator('github'))
        need_add_token = main.check_element_visible_by_locator(
            RepoPageLocators.ADD_TOKEN_BTN, 20)
        if need_add_token is True:
            main.click_with_delay(RepoPageLocators.ADD_TOKEN_BTN, 20)
            pass
        else:
            repos = main.find_all_elements(RepoPageLocators.ROWS_OF_REPO_TABLE, 30)
            print('There are {} repos can be added'.format(len(repos)))
            main.click_with_delay(RepoPageLocators.get_repo_row_locator(len(repos) - 1), 20)
            main.click_with_delay(RepoPageLocators.get_repo_row_locator(len(repos)), 20)
            main.click_with_delay(RepoPageLocators.get_repo_selected_chip_del_locator(0), 20)
            main.click(RepoPageLocators.ADD_REPO_BTN)
            main.click_with_delay(CommonLocators.SUCCESS_POPUP_BTN, 30)

    @unittest.skip("skip this test")
    def test_TC_RP_002(self):
        """
        Same with the flow from github but this one test with bitbucket cloud
        """
        # main = self.main
        # has_error = False
        pass

    @unittest.skip("skip this test")
    def test_TC_RP_003(self):
        """
        Same with the flow from github but this one test with gitlab cloud
        """
        # main = self.main
        # has_error = False
        pass

    @unittest.skip("skip this test")
    def test_TC_RP_004(self):
        """
        Same with the flow from github but this one test with Gerrit
        """
        # main = self.main
        # has_error = False
        pass

    @unittest.skip("skip this test")
    def test_TC_RP_005(self):
        """
        Test with adding repos from DevOps
        First will be check with username, token and base uri if added, and check if those
        values are valid
        Then showing the list of repos to add
        Choose the last repo from list
        And click add button to add
        Wait for the success popup
        """
        # main = self.main
        # has_error = False

    @unittest.skip("skip this test")
    def test_TC_RP_006(self):
        """
        Test with adding repos from Bitbucket Server
        Same with Devops flow but this will be test with Bitbucket Server
        """
        # main = self.main
        # has_error = False

    @unittest.skip("skip this test")
    def test_TC_RP_007(self):
        """
        Test with adding repos from Gitlab self-hosted
        Same with Devops flow but this will be test with Gitlab self-hosted
        """
        # main = self.main
        # has_error = False

    def test_TC_RP_008(self):
        """
        Test with deleting repos from repos list
        If there's any repos so delete the last repo from list
        else test will be stopped
        """
        main = self.main
        main.click_with_delay(RepoPageLocators.REPOSITORIES_TAB)
        main.rest_in_second(2)
        repos_items = main.find_all_elements(RepoPageLocators.REPO_ITEMS)
        init_len = len(repos_items)
        print(f'There are {len(repos_items)} in this project')
        if len(repos_items) > 0:
            main.click_with_delay(RepoPageLocators.get_repo_item_del_locator(
                len(repos_items) - 1))
            main.rest_in_second(5)
            repos_items = main.find_all_elements(RepoPageLocators.REPO_ITEMS, 30)
            if (len(repos_items)) >= init_len:
                raise Exception('Deleting repository failed')


if __name__ == '__main__':
    unittest.main()
