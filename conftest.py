import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


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
def base_url():
    """
    Фикстура с базовым URL приложения
    """
    return "https://stellarburgers.nomoreparties.site"
