from pages.base_page import BasePage
from locators.locators import AccountPageLocators


class AccountPage(BasePage):
    """Класс для страницы личного кабинета"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AccountPageLocators
    
    def click_logout_button(self):
        """Нажать кнопку 'Выход'"""
        self.click_element(self.locators.LOGOUT_BUTTON)
    
    def click_constructor_button(self):
        """Нажать кнопку 'Конструктор'"""
        self.click_element(self.locators.CONSTRUCTOR_BUTTON)
    
    def click_logo(self):
        """Нажать на логотип"""
        self.click_element(self.locators.LOGO)
    
    def is_profile_visible(self):
        """Проверить, отображается ли профиль (пользователь в ЛК)"""
        return self.is_element_visible(self.locators.PROFILE_LINK)
