from pages.base_page import BasePage
from locators.locators import ConstructorPageLocators


class ConstructorPage(BasePage):
    """Класс для страницы конструктора"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ConstructorPageLocators
    
    def click_buns_tab(self):
        """Нажать на вкладку 'Булки'"""
        self.click_element(self.locators.BUNS_TAB)
    
    def click_sauces_tab(self):
        """Нажать на вкладку 'Соусы'"""
        self.click_element(self.locators.SAUCES_TAB)
    
    def click_fillings_tab(self):
        """Нажать на вкладку 'Начинки'"""
        self.click_element(self.locators.FILLINGS_TAB)
    
    def is_constructor_loaded(self):
        """Проверить, загружен ли конструктор"""
        return self.is_element_visible(self.locators.CONSTRUCTOR_TITLE)
    
    def is_buns_section_visible(self):
        """Проверить видимость секции Булки"""
        return self.is_element_visible(self.locators.BUNS_SECTION)
    
    def is_sauces_section_visible(self):
        """Проверить видимость секции Соусы"""
        return self.is_element_visible(self.locators.SAUCES_SECTION)
    
    def is_fillings_section_visible(self):
        """Проверить видимость секции Начинки"""
        return self.is_element_visible(self.locators.FILLINGS_SECTION)
    
    def scroll_to_sauces(self):
        """Прокрутить до секции соусов"""
        self.scroll_to_element(self.locators.SAUCES_SECTION)
    
    def scroll_to_fillings(self):
        """Прокрутить до секции начинок"""
        self.scroll_to_element(self.locators.FILLINGS_SECTION)
