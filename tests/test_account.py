from pages.main_page import MainPage
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage
from locators.locators import ConstructorPageLocators
from urls import BASE_URL


class TestAccount:
    """Тесты личного кабинета"""
    
    def test_navigate_to_account(self, driver, authorized_user):
        """
        Проверка перехода в личный кабинет по клику на 'Личный кабинет'
        """
        driver.get(BASE_URL)
        
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.wait_for_url_contains("account")
        
        account_page = AccountPage(driver)
        assert account_page.is_profile_visible(), "Не удалось перейти в личный кабинет"
    
    def test_navigate_from_account_to_constructor_via_button(self, driver, authorized_user):
        """
        Проверка перехода из личного кабинета в конструктор
        по клику на кнопку 'Конструктор'
        """
        driver.get(BASE_URL)
        
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.wait_for_url_contains("account")
        
        account_page = AccountPage(driver)
        account_page.click_constructor_button()
        account_page.wait_for_element_visibility(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        
        constructor_page = ConstructorPage(driver)
        assert constructor_page.is_constructor_loaded(), "Не удалось перейти в конструктор"
    
    def test_navigate_from_account_to_constructor_via_logo(self, driver, authorized_user):
        """
        Проверка перехода из личного кабинета в конструктор
        по клику на логотип Stellar Burgers
        """
        driver.get(BASE_URL)
        
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.wait_for_url_contains("account")
        
        account_page = AccountPage(driver)
        account_page.click_logo()
        account_page.wait_for_element_visibility(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        
        constructor_page = ConstructorPage(driver)
        assert constructor_page.is_constructor_loaded(), "Не удалось перейти в конструктор"
    
    def test_logout(self, driver, authorized_user):
        """
        Проверка выхода из аккаунта по кнопке 'Выйти' в личном кабинете
        """
        driver.get(BASE_URL)
        
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.wait_for_url_contains("account")
        
        account_page = AccountPage(driver)
        account_page.click_logout_button()
        account_page.wait_for_url_contains("login")
        
        assert "login" in account_page.get_current_url(), "После выхода не произошел переход на страницу входа"
