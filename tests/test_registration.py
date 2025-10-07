from pages.registration_page import RegistrationPage
from helpers.generators import generate_email, generate_password, generate_invalid_password
from urls import REGISTER_URL


class TestRegistration:
    """Тесты регистрации пользователей"""

    def test_successful_registration(self, driver):
        """
        Проверка успешной регистрации с валидными данными:
        - Имя не пустое
        - Email в формате логин@домен
        - Пароль минимум 6 символов
        """
        driver.get(REGISTER_URL)
        
        reg_page = RegistrationPage(driver)
        
        name = "test"
        email = generate_email("ksenia", "barto", "30")
        password = generate_password(8)
        
        reg_page.register_user(name, email, password)
        reg_page.wait_for_url_contains("login")
        
        assert "login" in reg_page.get_current_url(), "Не произошел переход на страницу входа"
    
    def test_registration_with_invalid_password(self, driver):
        """
        Проверка ошибки при регистрации с некорректным паролем
        Пароль меньше 6 символов должен показывать ошибку
        """
        driver.get(REGISTER_URL)
        
        reg_page = RegistrationPage(driver)
        
        name = "Тест"
        email = generate_email("ksenia", "barto", "30")
        invalid_password = generate_invalid_password()
        
        reg_page.register_user(name, email, invalid_password)
        
        assert reg_page.is_password_error_visible(), "Ошибка для некорректного пароля не отображается"
