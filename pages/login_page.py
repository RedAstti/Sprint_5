from pages.base_page import BasePage
from locators.locators import LoginPageLocators


class LoginPage(BasePage):
    """Класс для страницы входа"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators
    
    def input_email(self, email):
        """Ввести email"""
        self.input_text(self.locators.EMAIL_INPUT, email)
    
    def input_password(self, password):
        """Ввести пароль"""
        self.input_text(self.locators.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Нажать кнопку 'Войти'"""
        self.click_element(self.locators.LOGIN_BUTTON)
    
    def click_register_link(self):
        """Нажать на ссылку 'Зарегистрироваться'"""
        self.click_element(self.locators.REGISTER_LINK)
    
    def click_restore_password_link(self):
        """Нажать на ссылку 'Восстановить пароль'"""
        self.click_element(self.locators.RESTORE_PASSWORD_LINK)
    
    def login_user(self, email, password):
        """Выполнить вход пользователя"""
        self.input_email(email)
        self.input_password(password)
        self.click_login_button()
