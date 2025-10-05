from pages.base_page import BasePage
from locators.locators import RestorePasswordPageLocators


class RestorePasswordPage(BasePage):
    """Класс для страницы восстановления пароля"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RestorePasswordPageLocators
    
    def click_login_link(self):
        """Нажать на ссылку 'Войти'"""
        self.click_element(self.locators.LOGIN_LINK)
