import unittest
from selenium import webdriver

# TODO
# All tests will log error and send to slack (?)


class TestBase(unittest.TestCase):
    # def setUp(self):
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument('headless')
    #     chrome_options.add_argument('window-size=1920x1080')
    #     self.driver = webdriver.Chrome(options=chrome_options)

    # def tearDown(self):
    #     self.driver.quit()
    #     self.driver.stop_client()

    # # TODO : Use below after done (for all other tests: SETUP REMOVE HERE)
    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.driver.stop_client()

    pass


if __name__ == '__main__':
    unittest.main()
