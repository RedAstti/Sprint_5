import pytest
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
import time


class TestConstructor:
    """Тесты раздела Конструктор"""
    
    def test_navigate_to_buns_section(self, driver, base_url):
        """
        Проверка перехода к разделу 'Булки'
        """
        driver.get(base_url)
        time.sleep(2)
        
        constructor_page = ConstructorPage(driver)
        
        # Сначала кликаем на другую вкладку
        constructor_page.click_sauces_tab()
        time.sleep(1)
        
        # Затем возвращаемся на Булки
        constructor_page.click_buns_tab()
        time.sleep(1)
        
        assert constructor_page.is_buns_section_visible(), "Раздел 'Булки' не отображается"
    
    def test_navigate_to_sauces_section(self, driver, base_url):
        """
        Проверка перехода к разделу 'Соусы'
        """
        driver.get(base_url)
        time.sleep(2)
        
        constructor_page = ConstructorPage(driver)
        constructor_page.click_sauces_tab()
        time.sleep(1)
        
        assert constructor_page.is_sauces_section_visible(), "Раздел 'Соусы' не отображается"
    
    def test_navigate_to_fillings_section(self, driver, base_url):
        """
        Проверка перехода к разделу 'Начинки'
        """
        driver.get(base_url)
        time.sleep(2)
        
        constructor_page = ConstructorPage(driver)
        constructor_page.click_fillings_tab()
        time.sleep(1)
        
        assert constructor_page.is_fillings_section_visible(), "Раздел 'Начинки' не отображается"
