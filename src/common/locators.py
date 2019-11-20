from selenium.webdriver.common.by import By


class CommonLocators():
    BREADCRUM = {
        'by': By.CSS_SELECTOR,
        'locator': '#ins-tour-breadcrum > li '
    }

    HAMBURGER_MENU = {
        'by': By.ID,
        'locator': 'btn-navbar-hamburger'}

    LOGOUT_BTN = {
        'by': By.ID,
        'locator': 'btn-logout'
    }

    SUCCESS_POPUP_BTN = {
        'by': By.ID,
        'locator': 'success-popup-btn'
    }

    ERROR_POPUP_BTN = {
        'by': By.ID,
        'locator': 'error-popup-btn'
    }


class LoginPageLocators():
    TITLE = {
        'by': By.XPATH,
        'locator': '//*[@id="root"]/div/div[2]/div[1]/div/h1'
    }

    RESET_PASSWORD_LINK = {
        'by': By.ID,
        'locator': 'reset-password-link-1'
    }

    RESET_PASSWORD_FORM = {
        'by': By.ID,
        'locator': 'reset-password-form'
    }

    RESET_PASSWORD_FORM_TEXT = {
        'by': By.CSS_SELECTOR,
        'locator': '#reset-password-form > div:nth-child(1) > div > h1'
    }

    RESET_PASSWORD_FORM_FIELD = {
        'by': By.ID,
        'locator': 'reset-pw-form-email'
    }

    RESET_PASSWORD_FORM_BTN = {
        'by': By.ID,
        'locator': 'reset-password-btn'
    }

    LOGIN_FORM_EMAIL = {
        'by': By.ID,
        'locator': 'input-email'
    }

    LOGIN_FORM_PASSWORD = {
        'by': By.ID,
        'locator': 'input-password'
    }

    LOGIN_FORM_REMEMBER_ME = {
        'by': By.ID,
        'locator': 'input-remember-me'
    }

    LOGIN_FORM_LOGIN_BTN = {
        'by': By.ID,
        'locator': 'btn-login'
    }

    ERROR_TEXT = {
        'by': By.ID,
        'locator': 'txt-login-error'
    }


class TeamPageLocators():
    APPBAR_TEXT = {
        'by': By.XPATH,
        'locator': '//*[@id="appbar-header"]/div/div[1]/div/div[2]/h1'
    }
    ADD_NEW_TEAM_FORM_FIELD = {
        'by': By.XPATH,
        'locator': '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div/div/div[2]'
        '/form/div[1]/div/div/input[@name="name"]'
    }
    ADD_NEW_TEAM_FORM_BTN = {
        'by': By.XPATH,
        'locator': '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div/div/div[2]'
        '/form/div[2]/button[@type="submit"]'
    }
    TEAM_LIST_ITEM = {
        'by': By.CSS_SELECTOR,
        'locator': '#ins-tour-team-list > li'
    }
    pass


class ProjectPageLocators():

    def get_project_item_text_locator(index):
        # index start from 1
        PROJECT_ITEM_TEXT = {
            'by': By.XPATH,
            'locator': f'//*[@id="ins-tour-project-list"]/li[{index}]/div[1]/div[2]/span/h2'
        }
        return PROJECT_ITEM_TEXT

    def get_project_item_locator(index):
        return {
            'by': By.XPATH,
            'locator': f'//*[@id="ins-tour-project-list"]/li[{index}]'
        }

    def get_project_item_delete_btn_locator(index):
        # index should start from 0
        PROJECT_ITEM_DELETE_BTN = {
            'by': By.ID,
            'locator': f'ins-tour-project-item-delete-{index}'
        }
        return PROJECT_ITEM_DELETE_BTN

    def get_project_item_settings_btn_locator(index):
        # index start from 0
        PROJECT_ITEM_SETTINGS_BTN = {
            'by': By.ID,
            'locator': f'inline-settings-btn-{index}'
        }
        return PROJECT_ITEM_SETTINGS_BTN

    def get_breadcrum_item_text_locator(index):
        BREADCRUM_TEXT = {
            'by': By.XPATH,
            'locator': f'//*[@id="ins-tour-breadcrum"]/li[{index}]/a'
        }
        return BREADCRUM_TEXT

    PROJECT_LIST = {
        'by': By.ID,
        'locator': 'ins-tour-project-list'
    }

    # elements from this locators will be return as Array and start from 0
    # return multi
    PROJECT_ITEMS = {
        'by': By.XPATH,
        'locator': '//*[@id="ins-tour-project-list"]/li'
    }

    APPBAR_TEXT = {
        'by': By.XPATH,
        'locator': '//*[@id="appbar-header"]/div/div[2]/h1'
    }

    GO_BACK_BTN = {
        'by': By.XPATH,
        'locator': '//*[@id="appbar-header"]/div/div[1]/div/div[1]/button'
    }

    CREATE_PROJECT_FORM_FIELD = {
        'by': By.ID,
        'locator': 'input-project-name'
    }

    CREATE_PROJECT_FORM_BTN = {
        'by': By.ID,
        'locator': 'btn-confirm-create-project'
    }

    DELETE_PROJECT_POPUP_CONFIRM_BTN = {
        'by': By.ID,
        'locator': 'confirm-delete-project-btn'
    }

    COPY_SETTINGS_BTN = {
        'by': By.ID,
        'locator': 'copy-settings-btn'
    }

    PASTE_SETTINGS_BTN = {
        'by': By.ID,
        'locator': 'paste-settings-btn'
    }

    pass


class RepoPageLocators():
    def get_add_repo_service_btn_locator(service):
        service_switcher = {
            'github': 1,
            'gitlab': 2,
            'gitlab_selfhost': 3,
            'bitbucket': 4,
            'bitbucket_server': 5,
            'azure': 6,
            'gerrit': 7,
            'custom': 8
        }
        locator_index = service_switcher.get(service, '8')
        return {
            'by': By.XPATH,
            'locator': f'//*[@id="ins-tour-add-repos-menu"]/div[2]/ul/li[{locator_index}]'
        }

    def get_repo_row_locator(index):
        # start from 1
        return {
            'by': By.XPATH,
            'locator': f'//*[@id="add-repo-table"]/tbody/tr[{index}]'
        }

    def get_repo_selected_chip_locator(index):
        # start from 0
        return {
            'by': By.ID,
            'locator': f'repo-selected-chip-{index}'
        }

    def get_repo_selected_chip_del_locator(index):
        # start from 0
        return {
            'by': By.CSS_SELECTOR,
            'locator': f'#repo-selected-chip-{index} > svg'
        }

    def get_repo_item_locator(index):
        # start from 0
        return {
            'by': By.ID,
            'locator': f'repo-list-item-{index}'
        }

    def get_repo_item_del_locator(index):
        # start from 0
        return {
            'by': By.ID,
            'locator': f'ins-tour-delete-repo-{index}'
        }

    APPBAR_TEXT = {
        'by': By.XPATH,
        'locator': '//*[@id="appbar-header"]/div/div[1]/div/div[2]/h1'
    }

    DELETE_PROJECT_BTN = {
        'by': By.ID,
        'locator': 'btn-delete-project'
    }

    PROJECT_SETTINGS_BTN = {
        'by': By.ID,
        'locator': 'ins-tour-project-settings-btn'
    }

    GO_BACK_BTN = {
        'by': By.XPATH,
        'locator': '//*[@id="appbar-header"]/div/div[1]/div/div[1]/button'
    }

    REPOSITORIES_TAB = {
        'by': By.ID,
        'locator': 'ins-tour-repo-list-tab'
    }

    KPI_TAB = {
        'by': By.ID,
        'locator': 'ins-tour-kpi-dashboard-tab'
    }

    REPORT_TAB = {
        'by': By.ID,
        'locator': 'ins-tour-report-list-tab'
    }

    # return multi
    REPO_ITEMS = {
        'by': By.CSS_SELECTOR,
        'locator': '#repo-list > li'
    }

    ADD_REPO_MENU_BTN = {
        'by': By.ID,
        'locator': 'ins-tour-add-repos-btn'
    }

    ADD_REPO_MENU = {
        'by': By.XPATH,
        'locator': '//*[@id="ins-tour-add-repos-menu"]/div[3]/ul'
    }

    ADD_TOKEN_BTN = {
        'by': By.ID,
        'locator': 'add-service-cloud-token-btn'
    }

    # return multi
    ROWS_OF_REPO_TABLE = {
        'by': By.XPATH,
        'locator': '//*[@id="add-repo-table"]/tbody/tr'
    }

    ADD_REPO_BTN = {
        'by': By.ID,
        'locator': 'add-repo-btn'
    }
    pass


class SettingsPageLocators():
    def get_selection_in_field(idx):
        # idx start from 1
        return {
            'by': By.XPATH,
            'locator': '//*[@id="menu-"]/div[2]/ul/li[{}]'.format(idx)
        }

    GO_BACK_BTN = {
        'by': By.XPATH,
        'locator': '//*[@id="appbar-header"]/div[1]/div/div[1]/button'
    }

    SAVE_BTN = {
        'by': By.ID,
        'locator': 'save-settings-btn'
    }

    ANALYSIS_FIELD = {
        'by': By.ID,
        'locator': 'analysis-panel-title'
    }

    AUTHENTICATION_FIELD = {
        'by': By.ID,
        'locator': 'auth-panel-title'
    }

    INTEGRATIONS_FIELD = {
        'by': By.ID,
        'locator': 'integrations-panel-title'
    }

    REPORT_FIELD = {
        'by': By.ID,
        'locator': 'report-panel-title'
    }

    KPI_FIELD = {
        'by': By.ID,
        'locator': 'kpi-panel-title'
    }

    BBSERVER_BASE_URI_INPUT_FIELD = {
        'by': By.ID,
        'locator': 'bbserver-base-uri-input'
    }

    BBSERVER_USERNAME_INPUT_FIELD = {
        'by': By.ID,
        'locator': 'bbserver-username-input'
    }

    BBSERVER_TOEKN_INPUT_FIELD = {
        'by': By.ID,
        'locator': 'bbserver-token-input'
    }

    GLSERVER_BASE_URI_INPUT_FIELD = {
        'by': By.ID,
        'locator': 'gitlabserver-base-uri-input'
    }

    GLSERVER_TOKEN_INPUT_FIELD = {
        'by': By.ID,
        'locator': 'gitlabserver-token-input'
    }

    TFS_BASE_URI_INPUT_FIELD = {
        'by': By.ID,
        'locator': 'tfs-base-uri-input'
    }

    TFS_USERNAME_INPUT_FIELD = {
        'by': By.ID,
        'locator': 'tfs-username-input'
    }

    TFS_TOKEN_INPUT_FIELD = {
        'by': By.ID,
        'locator': 'tfs-token-input'
    }

    EXCLUDE_FOLDER_INPUT_FIELD = {
        'by': By.ID,
        'locator': 'exclude-dir-chip-input'
    }

    LANGUAGE_TO_ANALYSE_SELECT_FIELD = {
        'by': By.XPATH,
        'locator': '//*[@id="select-language-analyse-select"]/div/div/div'
    }

    LANGUAGE_TO_EXCLUDE_SELECT_FIELD = {
        'by': By.XPATH,
        'locator': '//*[@id="select-language-to-exclude-select"]/div/div/div'
    }

    pass
