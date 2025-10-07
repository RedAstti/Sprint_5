from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    
    # Кнопка "Личный кабинет"
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")


class RegistrationPageLocators:
    """Локаторы страницы регистрации"""
    
    # Поле "Имя"
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    
    # Поле "Email"
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    
    # Поле "Пароль"
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    
    # Ссылка "Войти" (для перехода на страницу входа)
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    
    # Сообщение об ошибке для некорректного пароля
    PASSWORD_ERROR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")


class LoginPageLocators:
    """Локаторы страницы входа"""
    
    # Поле "Email"
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    
    # Поле "Пароль"
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль' or @type='password']")
    
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    
    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    
    # Ссылка "Восстановить пароль"
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")


class AccountPageLocators:
    """Локаторы страницы личного кабинета"""
    
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    
    # Ссылка на профиль (активная вкладка)
    PROFILE_LINK = (By.XPATH, "//a[contains(@class, 'Account_link') and contains(text(), 'Профиль')]")
    
    # Кнопка "Конструктор" в личном кабинете
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")


class ConstructorPageLocators:
    """Локаторы раздела Конструктор"""
    
    # Вкладка "Булки"
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    
    # Вкладка "Соусы"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    
    # Вкладка "Начинки"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    
    # Раздел с булками
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    
    # Раздел с соусами
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    
    # Раздел с начинками
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")
    
    # Заголовок "Соберите бургер"
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")


class RestorePasswordPageLocators:
    """Локаторы страницы восстановления пароля"""
    
    # Ссылка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
