import pytest
from pages.main_page import MainPage
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from pages.registration_page import RegistrationPage
from helpers.generators import generate_email, generate_password
import time


class TestAccount:
    """Тесты личного кабинета"""
    
    @pytest.fixture
    def authorized_user(self, driver, base_url):
        """Фикстура для создания и авторизации пользователя"""
        email = generate_email("ksenia", "barto", "30")
        password = generate_password(8)
        
        # Регистрация
        driver.get(f"{base_url}/register")
        reg_page = RegistrationPage(driver)
        reg_page.register_user("Пользователь", email, password)
        time.sleep(2)
        
        # Вход
        login_page = LoginPage(driver)
        login_page.login_user(email, password)
        time.sleep(2)
        
        return email, password
    
    def test_navigate_to_account(self, driver, base_url, authorized_user):
        """
        Проверка перехода в личный кабинет по клику на 'Личный кабинет'
        """
        driver.get(base_url)
        time.sleep(1)
        
        main_page = MainPage(driver)
        main_page.click_account_button()
        
        time.sleep(2)
        
        account_page = AccountPage(driver)
        assert account_page.is_profile_visible(), "Не удалось перейти в личный кабинет"
    
    def test_navigate_from_account_to_constructor_via_button(self, driver, base_url, authorized_user):
        """
        Проверка перехода из личного кабинета в конструктор 
        по клику на кнопку 'Конструктор'
        """
        # Сначала переходим на главную, затем в личный кабинет
        driver.get(base_url)
        time.sleep(1)
        
        main_page = MainPage(driver)
        main_page.click_account_button()
        time.sleep(2)
        
        # Теперь кликаем на Конструктор
        account_page = AccountPage(driver)
        account_page.click_constructor_button()
        time.sleep(2)
        
        constructor_page = ConstructorPage(driver)
        assert constructor_page.is_constructor_loaded(), "Не удалось перейти в конструктор"
    
    def test_navigate_from_account_to_constructor_via_logo(self, driver, base_url, authorized_user):
        """
        Проверка перехода из личного кабинета в конструктор 
        по клику на логотип Stellar Burgers
        """
        # Сначала переходим на главную, затем в личный кабинет
        driver.get(base_url)
        time.sleep(1)
        
        main_page = MainPage(driver)
        main_page.click_account_button()
        time.sleep(2)
        
        # Кликаем на логотип
        account_page = AccountPage(driver)
        account_page.click_logo()
        time.sleep(2)
        
        constructor_page = ConstructorPage(driver)
        assert constructor_page.is_constructor_loaded(), "Не удалось перейти в конструктор"
    
    def test_logout(self, driver, base_url, authorized_user):
        """
        Проверка выхода из аккаунта по кнопке 'Выйти' в личном кабинете
        """
        # Переходим в личный кабинет через интерфейс
        driver.get(base_url)
        time.sleep(1)
        
        main_page = MainPage(driver)
        main_page.click_account_button()
        time.sleep(2)
        
        # Выходим из аккаунта
        account_page = AccountPage(driver)
        account_page.click_logout_button()
        time.sleep(2)
        
        # После выхода должен быть редирект на страницу входа
        assert "login" in driver.current_url, "После выхода не произошел переход на страницу входа"
