import pytest
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from helpers.generators import generate_email, generate_password, generate_invalid_password
import time


class TestRegistration:
    """Тесты регистрации пользователей"""
    
    def test_successful_registration(self, driver, base_url):
        """
        Проверка успешной регистрации с валидными данными:
        - Имя не пустое
        - Email в формате логин@домен
        - Пароль минимум 6 символов
        """
        driver.get(f"{base_url}/register")
        
        reg_page = RegistrationPage(driver)
        
        name = "test"
        email = generate_email("ksenia", "barto", "30")
        password = generate_password(8)
        
        reg_page.register_user(name, email, password)
        
        # Ждем перехода на страницу входа после успешной регистрации
        time.sleep(2)
        
        login_page = LoginPage(driver)
        assert "login" in driver.current_url, "Не произошел переход на страницу входа"
    
    def test_registration_with_invalid_password(self, driver, base_url):
        """
        Проверка ошибки при регистрации с некорректным паролем
        Пароль меньше 6 символов должен показывать ошибку
        """
        driver.get(f"{base_url}/register")
        
        reg_page = RegistrationPage(driver)
        
        name = "Тест"
        email = generate_email("ksenia", "barto", "30")
        invalid_password = generate_invalid_password()
        
        reg_page.register_user(name, email, invalid_password)
        
        # Проверяем, что появилась ошибка
        time.sleep(1)
        assert reg_page.is_password_error_visible(), "Ошибка для некорректного пароля не отображается"
