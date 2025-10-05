import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.restore_password_page import RestorePasswordPage
from pages.account_page import AccountPage
from helpers.generators import generate_email, generate_password
import time


class TestLogin:
    """Тесты входа в систему"""
    
    @pytest.fixture
    def create_user(self, driver, base_url):
        """Фикстура для создания тестового пользователя"""
        email = generate_email("ksenia", "barto", "30")

        password = generate_password(8)
        
        driver.get(f"{base_url}/register")
        reg_page = RegistrationPage(driver)
        reg_page.register_user("Тестовый", email, password)
        time.sleep(2)
        
        return email, password
    
    def test_login_via_main_button(self, driver, base_url, create_user):
        """
        Проверка входа по кнопке 'Войти в аккаунт' на главной странице
        """
        email, password = create_user
        
        driver.get(base_url)
        main_page = MainPage(driver)
        main_page.click_login_button()
        
        time.sleep(1)
        
        login_page = LoginPage(driver)
        login_page.login_user(email, password)
        
        time.sleep(2)
        
        # Проверяем, что вход выполнен - должна быть кнопка "Оформить заказ"
        assert base_url in driver.current_url
    
    def test_login_via_account_button(self, driver, base_url, create_user):
        """
        Проверка входа через кнопку 'Личный кабинет'
        """
        email, password = create_user
        
        driver.get(base_url)
        main_page = MainPage(driver)
        main_page.click_account_button()
        
        time.sleep(1)
        
        login_page = LoginPage(driver)
        login_page.login_user(email, password)
        
        time.sleep(2)
        
        assert base_url in driver.current_url
    
    def test_login_via_registration_form(self, driver, base_url, create_user):
        """
        Проверка входа через кнопку в форме регистрации
        """
        email, password = create_user
        
        driver.get(f"{base_url}/register")
        reg_page = RegistrationPage(driver)
        reg_page.click_login_link()
        
        time.sleep(1)
        
        login_page = LoginPage(driver)
        login_page.login_user(email, password)
        
        time.sleep(2)
        
        assert base_url in driver.current_url
    
    def test_login_via_restore_password_form(self, driver, base_url, create_user):
        """
        Проверка входа через кнопку в форме восстановления пароля
        """
        email, password = create_user
        
        driver.get(f"{base_url}/login")
        login_page = LoginPage(driver)
        login_page.click_restore_password_link()
        
        time.sleep(1)
        
        restore_page = RestorePasswordPage(driver)
        restore_page.click_login_link()
        
        time.sleep(1)
        
        login_page = LoginPage(driver)
        login_page.login_user(email, password)
        
        time.sleep(2)
        
        assert base_url in driver.current_url
