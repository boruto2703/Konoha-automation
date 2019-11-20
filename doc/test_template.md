### Name
- with prefix: text_TC_
- page name in short (Team page = TP, Project page = PP, etc.)
- test number
example: `test_TC_RP_001`

### Add test case
- with detail description below test name
For example: 
```
    def test_TC_TP_001(self):
        """
        Load teams list page 
        By: Find the element after login 
        Check the breadcrums text
        Check from the toolbar
        """
```
- Add short description in [README.md](../README.md)
- We use unittest to run the selenium test, so we would add the setup (common part to navigate to page)
- Result will be use to add to slack

### Common used functions
Functions in this file: [pages.py](../src/common/pages.py)
For setting up new test page:
- Create new class in [pages.py](../src/common/pages.py) with name: `class PageName(UpperPage)` - `UpperPage` is the class name of upper page (For example: ProjectListPage is the RepoListPage)
- `CommonPage` contains common functions used in other pages
In `setUpClass()` in each test page: add `self.main = PageName(self.driver)`