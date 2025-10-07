import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from locators.locators import MainPageLocators
from helpers.generators import generate_email, generate_password
from urls import REGISTER_URL


@pytest.fixture
def driver():
    """
    Фикстура для создания и закрытия браузера Chrome
    Автоматически запускается перед каждым тестом и закрывается после
    """
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    browser.implicitly_wait(3)
    
    yield browser
    
    browser.quit()


@pytest.fixture
def create_user(driver):
    """Фикстура для создания тестового пользователя"""
    email = generate_email("ksenia", "barto", "30")
    password = generate_password(8)
    
    driver.get(REGISTER_URL)
    reg_page = RegistrationPage(driver)
    reg_page.register_user("Тестовый", email, password)
    reg_page.wait_for_url_contains("login")
    
    return email, password


@pytest.fixture
def authorized_user(driver):
    """Фикстура для создания и авторизации пользователя"""
    email = generate_email("ksenia", "barto", "30")
    password = generate_password(8)

    driver.get(REGISTER_URL)
    reg_page = RegistrationPage(driver)
    reg_page.register_user("Пользователь", email, password)
    reg_page.wait_for_url_contains("login")
    
    login_page = LoginPage(driver)
    login_page.login_user(email, password)
    login_page.wait_for_element_invisibility(MainPageLocators.LOGIN_BUTTON_MAIN)
    
    return email, password
