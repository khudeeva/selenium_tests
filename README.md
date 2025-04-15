# Selenium Tests 🧪

Проект с автотестами на Python + Selenium для тренировки навыков UI-тестирования.

## 🔧 Технологии

- Python 3.13
- Selenium WebDriver
- WebDriver Manager
- PyTest
- logging (для логирования)
- Скриншоты при ошибках

---

## 📁 Структура проекта

```
selenium-tests/
│
├── tests/
│   ├── alerts/                 # Тесты для alert / confirm / prompt окон
│   ├── forms/                  # Тесты для форм: чекбоксы, радиокнопки, выпадающие списки
│   ├── frames/                 # Тесты для вложенных и одиночных фреймов
│   ├── tabs_windows/           # Тесты на переключение между окнами и вкладками
│   └── login/                  # Логин-тесты: валидные и невалидные сценарии
│
├── chromedriver.exe           # WebDriver (в .gitignore, не добавлять в репозиторий)
├── requirements.txt           # Зависимости
├── README.md                  # Этот файл
```

---

## 🚀 Как запустить

1. Установить зависимости:

```bash
pip install -r requirements.txt
```

2. Запуск всех тестов:

```bash
pytest tests/
```

3. Запуск конкретной категории (например, alerts):

```bash
pytest tests/alerts/
```

4. Запуск конкретного файла:

```bash
pytest tests/login/test_valid_login.py
```

---

## 🖼 Скриншоты и логирование

- При падении теста делается скриншот и сохраняется в `selenium-tests/`
- Лог записывается в `test_log.log`

---

## 📌 Автор khudeeva

Учебный проект по UI-автоматизации. Выполнено вручную для отработки навыков с Selenium и PyTest.
