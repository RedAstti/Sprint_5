from pages.base_page import BasePage
from locators.locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    """Класс для страницы регистрации"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RegistrationPageLocators
    
    def input_name(self, name):
        """Ввести имя"""
        self.input_text(self.locators.NAME_INPUT, name)
    
    def input_email(self, email):
        """Ввести email"""
        self.input_text(self.locators.EMAIL_INPUT, email)
    
    def input_password(self, password):
        """Ввести пароль"""
        self.input_text(self.locators.PASSWORD_INPUT, password)
    
    def click_register_button(self):
        """Нажать кнопку 'Зарегистрироваться'"""
        self.click_element(self.locators.REGISTER_BUTTON)
    
    def click_login_link(self):
        """Нажать на ссылку 'Войти'"""
        self.click_element(self.locators.LOGIN_LINK)
    
    def is_password_error_visible(self):
        """Проверить, отображается ли ошибка для некорректного пароля"""
        return self.is_element_visible(self.locators.PASSWORD_ERROR)
    
    def register_user(self, name, email, password):
        """Выполнить регистрацию пользователя"""
        self.input_name(name)
        self.input_email(email)
        self.input_password(password)
        self.click_register_button()
