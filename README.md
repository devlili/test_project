[![Python](https://img.shields.io/badge/-Python_3.8-464646??style=flat-square&logo=Python)](https://www.python.org/downloads/)
[![Pytest](https://img.shields.io/badge/-Pytest_7.1.2-464646??style=flat-square&logo=Pytest)](https://docs.pytest.org/en/7.1.x/)
[![Selenium](https://img.shields.io/badge/-Selenium_4.3.0-464646??style=flat-square&logo=Selenium)](https://www.selenium.dev/)

# Проект с автотестами
Данный проект представляет собой автоматизированные тесты для проверки работоспособности интернет-магазина. Тесты реализованы на Pytest и Selenium, используя паттерн проектирования Page Object Model.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/devlili/test_project.git
```

```
cd test_project
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env  # Команда для Linux и macOS
python -m venv venv  # Команда для Windows
```

```
source env/bin/activate  # Команда для Linux и macOS
source venv/Scripts/activate  # Команда для Windows
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## Запуск автотестов

 Для запуска всех автотестов выполните следующую команду:
 ```
 pytest
 ```
## Автор
Лилия Альмухаметова
