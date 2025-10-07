from pages.constructor_page import ConstructorPage
from locators.locators import ConstructorPageLocators
from urls import BASE_URL


class TestConstructor:
    """Тесты раздела Конструктор"""

    def test_navigate_to_buns_section(self, driver):
        """
        Проверка перехода к разделу 'Булки'
        """
        driver.get(BASE_URL)
        
        constructor_page = ConstructorPage(driver)
        constructor_page.wait_for_element_visibility(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        
        constructor_page.click_sauces_tab()
        constructor_page.wait_for_element_visibility(ConstructorPageLocators.SAUCES_SECTION)
        
        constructor_page.click_buns_tab()
        constructor_page.wait_for_element_visibility(ConstructorPageLocators.BUNS_SECTION)
        
        assert constructor_page.is_buns_section_visible(), "Раздел 'Булки' не отображается"
    
    def test_navigate_to_sauces_section(self, driver):
        """
        Проверка перехода к разделу 'Соусы'
        """
        driver.get(BASE_URL)
        
        constructor_page = ConstructorPage(driver)
        constructor_page.wait_for_element_visibility(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        
        constructor_page.click_sauces_tab()
        constructor_page.wait_for_element_visibility(ConstructorPageLocators.SAUCES_SECTION)
        
        assert constructor_page.is_sauces_section_visible(), "Раздел 'Соусы' не отображается"
    
    def test_navigate_to_fillings_section(self, driver):
        """
        Проверка перехода к разделу 'Начинки'
        """
        driver.get(BASE_URL)
        
        constructor_page = ConstructorPage(driver)
        constructor_page.wait_for_element_visibility(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        
        constructor_page.click_fillings_tab()
        constructor_page.wait_for_element_visibility(ConstructorPageLocators.FILLINGS_SECTION)
        
        assert constructor_page.is_fillings_section_visible(), "Раздел 'Начинки' не отображается"
