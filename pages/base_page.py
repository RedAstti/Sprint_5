from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Найти элемент на странице"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_element_clickable(self, locator):
        """Дождаться, пока элемент станет кликабельным"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def click_element(self, locator):
        """Кликнуть по элементу"""
        element = self.find_element_clickable(locator)
        element.click()
    
    def input_text(self, locator, text):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Получить текст элемента"""
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator, timeout=5):
        """Проверить, виден ли элемент"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    def scroll_to_element(self, locator):
        """Прокрутить страницу до элемента"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url
