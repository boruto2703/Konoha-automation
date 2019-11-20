import unittest
import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.common.errors import NotFoundError, UnClickableError, TypeError
from src.common.locators import RepoPageLocators, \
    ProjectPageLocators, CommonLocators, LoginPageLocators


with open('src/json/names.json', 'r') as namefile:
    data = namefile.read()
    names = json.loads(data)

with open('src/json/integrations.json', 'r') as integrationsfile:
    data = integrationsfile.read()
    integrations = json.loads(data)

with open('src/json/auth.json', 'r') as authfile:
    data = authfile.read()
    auth = json.loads(data)


class CommonPage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://df.softagram.com')
        self.array_of_test = []

    """
    Find elements functions
    """

    def find_element_with_wait(self, locator: object, custom_time=10):
        ele = WebDriverWait(self.driver, custom_time).until(
            EC.visibility_of_element_located((locator['by'], locator['locator'])))
        return ele

    def find_all_elements(self, locator, custom_time=15):
        elements = WebDriverWait(self.driver, custom_time).until(
            EC.visibility_of_all_elements_located((locator['by'], locator['locator'])))
        return elements

    """
    Click action
    """

    def click(self, locator):
        ele = self.driver.find_element(locator['by'], locator['locator'])
        ActionChains(self.driver).move_to_element(ele).click().perform()

    def click_with_delay(self, locator, custom_time=10):
        try:
            ele = WebDriverWait(self.driver, custom_time).until(
                EC.element_to_be_clickable((locator['by'], locator['locator'])))
            ActionChains(self.driver).move_to_element(ele).click().perform()
        except TimeoutException:
            raise UnClickableError
        except Exception:
            raise UnClickableError

    def click_if_posible(self, locator, custom_time=10):
        is_visible = self.check_element_visible_by_locator(locator, custom_time)
        is_enable = self.check_element_enable_by_locator(locator, custom_time)
        if is_visible is True and is_enable is True:
            self.click(locator)
        else:
            print(
                f'Cannot perform click action because the element with locator ({locator}) '
                'is not found')
            raise NotFoundError

    """
    Input action
    """

    def clear_field(self, locator):
        ele = self.find_element_with_wait(locator)
        val = ele.get_attribute('value')
        length = len(val)
        for i in range(length):
            self.find_element_with_wait(locator).send_keys(Keys.BACKSPACE)
        pass

    def input_to_field(self, locator, value, clear_field=False):
        if clear_field is True:
            self.clear_field(locator)
        self.find_element_with_wait(locator).send_keys(value)

    """
    Check if elements meet the conditions
    """

    def check_if_element_is_clickable(self, locator, custom_time=10):
        try:
            WebDriverWait(self.driver, custom_time).until(
                EC.element_to_be_clickable((locator['by'], locator['locator'])))
            return True
        except Exception:
            return False

    def check_invisibility_of_dialog(self, locator, custom_time=10):
        WebDriverWait(self.driver, custom_time).until(
            EC.invisibility_of_element_located((locator['by'], locator['locator'])))

    def check_element_enable(self, ele):
        return ele.is_enabled()

    def check_element_enable_by_locator(self, locator, custom_time=10):
        try:
            ele = self.find_element_with_wait(locator, custom_time)
            return self.check_element_enable(ele)
        except Exception:
            return False

    def check_element_visible_by_locator(self, locator, custom_time=10):
        try:
            self.find_element_with_wait(locator, custom_time)
            return True
        except Exception:
            return False

    """
    Other mouse action
    """

    def hover(self, locator, custom_time=10):
        ele = WebDriverWait(self.driver, custom_time).until(
            EC.visibility_of_element_located((locator['by'], locator['locator'])))
        ActionChains(self.driver).move_to_element(ele).perform()

    """
    Assert text
    """

    def get_element_text(self, locator, custom_time=10, pos=None):
        if pos is None:
            ele = WebDriverWait(self.driver, custom_time).until(
                EC.visibility_of_element_located((locator['by'], locator['locator'])))
            return ele.text.lower()
        elif type(pos) is int:
            elements = WebDriverWait(self.driver, custom_time).until(
                EC.visibility_of_any_elements_located((locator['by'], locator['locator'])))
            return elements[pos].text.lower()
        else:
            raise TypeError('TypeError: pos should be integer')

    def assert_element_text(self, locator, value, custom_time=15):
        text = self.get_element_text(locator, custom_time)
        assert value.lower() in text

    def compare_element_text(self, locator, value, custom_time=15):
        text = self.get_element_text(locator, custom_time)
        return value.lower() in text

    def assert_element_text_in_group(self, locator, pos, value, custom_time=10):
        text = self.get_element_text(locator, custom_time, pos)
        assert value.lower() in text

    def compare_element_text_in_group(self, locator, pos, value, custom_time=10):
        text = self.get_element_text(locator, custom_time, pos)
        return value.lower() in text

    """
    Other
    """

    def rest_in_second(self, sec):
        time.sleep(sec)


class LoginPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email=auth['email'], password=auth['password']):
        try:
            super().input_to_field(LoginPageLocators.LOGIN_FORM_EMAIL, email)
            super().input_to_field(LoginPageLocators.LOGIN_FORM_PASSWORD, password)
            super().click(LoginPageLocators.LOGIN_FORM_REMEMBER_ME)
            super().click_with_delay(LoginPageLocators.LOGIN_FORM_LOGIN_BTN)
        except NoSuchElementException:
            print('Element missing in login form')
        except Exception:
            print('Failed to login')


class TeamPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)


class ProjectPage(TeamPage):
    def __init__(self, driver):
        super().__init__(driver)

    def create_new_project(self, skipTest, name=names["new_project"]):
        btn_create_project = super().find_element_with_wait(
            {'by': By.ID, 'locator': 'btn-create-project'})

        enable_to_create_project = super().check_element_enable(btn_create_project)
        if enable_to_create_project is True:
            btn_create_project.click()
            super().input_to_field(ProjectPageLocators.CREATE_PROJECT_FORM_FIELD, name)
            super().click_with_delay(ProjectPageLocators.CREATE_PROJECT_FORM_BTN)

            try:
                super().click_with_delay(CommonLocators.SUCCESS_POPUP_BTN)
            except NotFoundError:
                try:
                    super().click_with_delay(CommonLocators.ERROR_POPUP_BTN)
                    raise Exception(f'Cannot create new project with name {name}')
                except NotFoundError:
                    pass

            super().assert_element_text(RepoPageLocators.APPBAR_TEXT, name)

        else:
            print('Skip test because user cannot create new project')
            if skipTest:
                skipTest('Skip Test because user is not admin')

    def find_project_index_by_name(self, name=names["new_project"]):
        project_items = super().find_all_elements(ProjectPageLocators.PROJECT_ITEMS, 20)
        project_idx = 0
        found_idx = False
        for i in range(len(project_items)):
            project_name_locator = ProjectPageLocators.get_project_item_text_locator(i + 1)
            if super().compare_element_text(project_name_locator, name):
                project_idx = i
                found_idx = True
                break
        return found_idx, project_idx

    def find_and_delete_project(self, name=names["new_project"]):
        found_idx, project_idx = self.find_project_index_by_name(name)

        if found_idx is False:
            raise Exception(f'No project with name {name} found to delete')
            pass
        else:
            del_btn_locator = ProjectPageLocators.get_project_item_delete_btn_locator(
                project_idx)
            super().click_with_delay(del_btn_locator)
            super().click_if_posible(ProjectPageLocators.DELETE_PROJECT_POPUP_CONFIRM_BTN)
            super().click_if_posible(CommonLocators.SUCCESS_POPUP_BTN)
            print(f'Project with name {name} deleted!')


class RepoPage(ProjectPage):
    def __init__(self, driver):
        super().__init__(driver)

    pass


if __name__ == '__main__':
    unittest.main()
