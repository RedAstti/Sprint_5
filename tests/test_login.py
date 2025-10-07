from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.restore_password_page import RestorePasswordPage
from locators.locators import MainPageLocators
from urls import BASE_URL, REGISTER_URL, LOGIN_URL


class TestLogin:
    """Тесты входа в систему"""
    
    def test_login_via_main_button(self, driver, create_user):
        """
        Проверка входа по кнопке 'Войти в аккаунт' на главной странице
        """
        email, password = create_user
        
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        main_page.click_login_button()
        main_page.wait_for_url_contains("login")
        
        login_page = LoginPage(driver)
        login_page.login_user(email, password)
        login_page.wait_for_element_visibility(MainPageLocators.ACCOUNT_BUTTON)
        
        assert BASE_URL in login_page.get_current_url()
    
    def test_login_via_account_button(self, driver, create_user):
        """
        Проверка входа через кнопку 'Личный кабинет'
        """
        email, password = create_user
        
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.wait_for_url_contains("login")
        
        login_page = LoginPage(driver)
        login_page.login_user(email, password)
        login_page.wait_for_element_visibility(MainPageLocators.ACCOUNT_BUTTON)
        
        assert BASE_URL in login_page.get_current_url()
    
    def test_login_via_registration_form(self, driver, create_user):
        """
        Проверка входа через кнопку в форме регистрации
        """
        email, password = create_user
        
        driver.get(REGISTER_URL)
        reg_page = RegistrationPage(driver)
        reg_page.click_login_link()
        reg_page.wait_for_url_contains("login")
        
        login_page = LoginPage(driver)
        login_page.login_user(email, password)
        login_page.wait_for_element_visibility(MainPageLocators.ACCOUNT_BUTTON)
        
        assert BASE_URL in login_page.get_current_url()
    
    def test_login_via_restore_password_form(self, driver, create_user):
        """
        Проверка входа через кнопку в форме восстановления пароля
        """
        email, password = create_user
        
        driver.get(LOGIN_URL)
        login_page = LoginPage(driver)
        login_page.click_restore_password_link()
        login_page.wait_for_url_contains("forgot-password")
        
        restore_page = RestorePasswordPage(driver)
        restore_page.click_login_link()
        restore_page.wait_for_url_contains("login")
        
        login_page = LoginPage(driver)
        login_page.login_user(email, password)
        login_page.wait_for_element_visibility(MainPageLocators.ACCOUNT_BUTTON)
        
        assert BASE_URL in login_page.get_current_url()
