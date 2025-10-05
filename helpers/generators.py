import random
import string


def generate_email(name="test", surname="testov", cohort="99"):
    random_digits = ''.join(random.choices(string.digits, k=3))
    email = f"{name}_{surname}_{cohort}_{random_digits}@ya.ru"
    return email


def generate_password(length=6):
    if length < 6:
        length = 6
    
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=length))
    return password


def generate_invalid_password():
    return ''.join(random.choices(string.ascii_letters, k=5))
