import json
import unittest
import os

from src.common.TestBase import TestBase
from src.common.pages import LoginPage
from src.common.locators import LoginPageLocators, CommonLocators

with open('src/json/auth.json', 'r') as authfile:
    data = authfile.read()
    auth = json.loads(data)

auth = {
    'email': os.environ.get('TEST_EMAIL'),
    'password': os.environ.get('')
}


class TestLoginPage(TestBase):

    def setUp(self):
        self.main = LoginPage(self.driver)

    def test_TC_L_001(self):
        """
        Load login page success (without internal server error)
        """
        self.main.assert_element_text(LoginPageLocators.TITLE, 'Softagram')
        print(f' % {self._testMethodName}: Success % ')

    # @unittest.skip('Skip because this step will be show in later tests')
    def test_TC_L_002(self):
        """
        Test login case with correct username and password
        """

        main = self.main

        main.login()
        # logout
        main.click_with_delay(CommonLocators.HAMBURGER_MENU)
        main.click(CommonLocators.LOGOUT_BTN)
        # wait
        main.assert_element_text(LoginPageLocators.TITLE, 'Softagram')
        print(f' % {self._testMethodName}: Success % ')

    def test_TC_L_003(self):
        """
        Test login case with wrong username and password
        """
        main = self.main
        main.login(auth['email'], auth['wrong_password'])
        # login failed
        main.assert_element_text(LoginPageLocators.ERROR_TEXT, 'Invalid password or email!')
        print(f' % {self._testMethodName}: Success % ')

    def test_TC_L_004(self):
        """
        Test reset password if worked
        """
        main = self.main
        main.click(LoginPageLocators.RESET_PASSWORD_LINK)
        main.assert_element_text(
            LoginPageLocators.RESET_PASSWORD_FORM_TEXT, 'Reset Password')
        main.input_to_field(
            LoginPageLocators.RESET_PASSWORD_FORM_FIELD,
            auth['email'])
        main.click(LoginPageLocators.RESET_PASSWORD_FORM_BTN)
        main.check_invisibility_of_dialog(LoginPageLocators.RESET_PASSWORD_FORM)
        print(f' % {self._testMethodName}: Success % ')


if __name__ == '__main__':
    unittest.main()
