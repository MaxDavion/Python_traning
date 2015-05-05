# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture


fixture = None
target = None  # Определяем переменную для конфиг файла target.json

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)  # Строим путь до конфиг файла, относительно директории проекта
        with open(config_file) as f:
            target = json.load(f)  # Читаем конфиг-файл, загружая из него указанные там параметры (в виде target[ключ]), для дальнейшего использования
    return target


# Фикстура для Браузера
@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")  # Передаем браузер в конструктор класса Application
    web_config = load_config(request.config.getoption("--target"))["web"]
    #  Проверяем  существует ли фикстура и корректная ли она, если нет то создаем новую
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    # Выполняем авторизацию в приложении
    fixture.session.ensure_login(user=web_config["user"], password=web_config["password"])
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


# Фикстура для Базы Данных
@pytest.fixture(scope='session')
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=db_config["host"], database=db_config["database"], user=db_config["user"], password=db_config["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

# Фикстура для отключаемых проверок UI
@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


#  Опции для запуска командной строкой
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")  # Доавляет возможность указывать браузер на котором запускать. По умолчанию FireFox
    parser.addoption("--target", action="store", default="target.json")  # Добавляет возможность указывать конфиг. файл. По умолчанию target.json
    parser.addoption("--check_ui", action="store_true")


# Функция обеспечивает динамическое связывание данных с тестами через фикстуру
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


# Загружает данные из data/модуля с заданным именем
def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

# Загружает данные из data/json-файла с заданным именем
def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())