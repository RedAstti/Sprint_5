from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):
    """Класс для главной страницы"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators
    
    def click_login_button(self):
        """Нажать на кнопку 'Войти в аккаунт'"""
        self.click_element(self.locators.LOGIN_BUTTON_MAIN)
    
    def click_account_button(self):
        """Нажать на кнопку 'Личный кабинет'"""
        self.click_element(self.locators.ACCOUNT_BUTTON)
    
    def click_constructor_button(self):
        """Нажать на кнопку 'Конструктор'"""
        self.click_element(self.locators.CONSTRUCTOR_BUTTON)
    
    def click_logo(self):
        """Нажать на логотип"""
        self.click_element(self.locators.LOGO)
    
    def is_main_page_loaded(self):
        """Проверить, загружена ли главная страница"""
        return self.is_element_visible(self.locators.LOGIN_BUTTON_MAIN)
