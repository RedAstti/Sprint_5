# Sprint 5 - Автотесты для Stellar Burgers

Проект автоматизации тестирования веб-приложения Stellar Burgers с использованием Selenium WebDriver.

## Описание

Проект содержит автотесты для проверки основной функциональности:
- Регистрация пользователей
- Вход в систему (различные способы)
- Личный кабинет
- Навигация по конструктору бургеров

## Структура проекта

```
Sprint5/
├── locators/           # Локаторы элементов страниц
├── pages/              # Page Object классы
├── helpers/            # Вспомогательные функции
├── tests/              # Тестовые сценарии
├── conftest.py         # Фикстуры pytest
├── urls.py             # URL's для тестов
└── requirements.txt    # Зависимости
```

## Установка

1. Клонируйте репозиторий
2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Убедитесь, что установлен Google Chrome

## Запуск тестов

Запуск всех тестов:
```bash
pytest tests/
```

Запуск конкретного файла с тестами:
```bash
pytest tests/test_registration.py
```

Запуск с подробным выводом:
```bash
pytest tests/ -v
```

## Технологии

- Python 3.x
- Selenium WebDriver
- Pytest
- Chrome WebDriver

## Автор

Проект выполнен в рамках обучения на курсе автоматизации тестирования.
