import unittest
# from concurrencytest import ConcurrencyTestSuite, fork_for_tests
from src.tests.TestLoginPage import TestLoginPage
from src.tests.TestTeamListPage import TestTeamListPage
from src.tests.TestProjectListPage import TestProjectListPage
from src.tests.TestRepoListPage import TestRepoListPage


def suite():
    suite = unittest.TestSuite()
    # Login Page tests
    suite.addTest(TestLoginPage('test_TC_L_001'))
    suite.addTest(TestLoginPage('test_TC_L_003'))
    suite.addTest(TestLoginPage('test_TC_L_004'))
    # Dashboard / Team page
    suite.addTest(TestTeamListPage('test_TC_TP_001'))
    suite.addTest(TestTeamListPage('test_TC_TP_002'))
    # Project Page
    suite.addTest(TestProjectListPage('test_TC_PP_001'))
    suite.addTest(TestProjectListPage('test_TC_PP_004'))
    suite.addTest(TestProjectListPage('test_TC_PP_005'))
    suite.addTest(TestProjectListPage('test_TC_PP_006'))
    # Repos Page
    suite.addTest(TestRepoListPage('test_TC_RP_001'))
    suite.addTest(TestRepoListPage('test_TC_RP_008'))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    # concurrency_suite = ConcurrencyTestSuite(suite, fork_for_tests(2))
    runner.run(suite)
