# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
import json
import os.path

fixture = None
target = None  # Определяем переменную для конфиг файла target.json

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")  # Передаем браузер в конструктор класса Application
    #  При создании фикстуры
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))  # Строим путь до конфиг файла, относительно директории проекта (директория с текущим файлом (conftest.py) +  конфиг-файл)
        with open(config_file) as f:
            target = json.load(f)  # Читаем конфиг-файл, загружая из него указанные там параметры (в виде target[ключ]), для дальнейшего использования.
    #  Проверяем  существует ли фикстура и корректная ли она, если нет то создаем новую
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])
    # Выполняем авторизацию в приложении
    fixture.session.ensure_login(user=target["user"], password=target["password"])
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


#  Опции для запуска командной строкой
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")  # Доавляет возможность указывать браузер на котором запускать. По умолчанию FireFox
    parser.addoption("--target", action="store", default="target.json")  # Добавляет возможность указывать конфиг. файл. По умолчанию target.json