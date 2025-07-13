# 🧑‍💻 User Profiles CLI App

Простой консольный Python-проект для управления профилями пользователей. Поддерживает создание, просмотр, фильтрацию, удаление и экспорт в CSV. Структура кода организована по модулям и включает тесты.

---

## 🚀 Возможности

* ✅ Создание пользовательского профиля
* 📋 Просмотр всех пользователей
* 🔍 Поиск по имени (нечувствительный к регистру)
* 🗑️ Удаление по имени
* 📤 Экспорт данных в CSV

---

## 🧱 Стек технологий

* Python 3.12+
* `argparse` — CLI
* `dataclasses` — модель пользователя
* `json` / `csv` — хранение данных
* `pytest` — тесты
* `ruff` — линтинг

---

## 🔧 Установка и запуск

1. Клонируй репозиторий:

```bash
git clone https://github.com/iRatatuii/py-utils.git
cd py-utils
```

2. Установи зависимости:

```bash
uv sync 
```

или

```bash
make install 
```

3. Запусти программу:

```bash
uv run utils create     # Создать пользователя
uv run utils list       # Показать всех
uv run utils filter --query "Имя"
uv run utils delete --name "Имя"
uv run utils export --out users.csv
```

---

## 🧪 Тестирование

```bash
uv run pytest
```

или

```bash
make test
```

---

## 👨‍🎓 Автор

Разработано в рамках обучения Python и бэкенд-разработке. Автор: [Andrey (iRatatuii)](https://github.com/iRatatuii)

---

## 📄 Лицензия

Проект распространяется под лицензией MIT.
