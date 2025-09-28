# 🐍 Django — шпаргалка по командам CLI

Этот файл содержит основные команды для работы с Django из командной строки.

---

## 🚀 Быстрый старт Django
```bash
# Установить Django
pip install django

# Создать проект
django-admin startproject myproject
cd myproject

# Создать приложение
python manage.py startapp myapp

# Запустить сервер разработки
python manage.py runserver
```
После этого проект будет доступен по адресу: http://127.0.0.1:8000/

---

## 🚀 Управление проектом
```bash
# Создать новый проект
django-admin startproject myproject

# Создать новое приложение
python manage.py startapp myapp

# Запуск сервера разработки (по умолчанию localhost:8000)
python manage.py runserver

# Запуск сервера на другом порту
python manage.py runserver 8080

# Проверка проекта на ошибки
python manage.py check
```

---

## 🗂 Работа с миграциями
```bash
# Создать миграции на основе изменений моделей
python manage.py makemigrations

# Применить миграции к базе
python manage.py migrate

# Показать список миграций
python manage.py showmigrations

# Посмотреть SQL конкретной миграции
python manage.py sqlmigrate app_name 0001
```

---

## 👤 Работа с пользователями и админкой
```bash
# Создать суперпользователя
python manage.py createsuperuser
```

---

## 💾 Работа с базой данных
```bash
# Открыть shell Django (ORM)
python manage.py shell

# Использовать расширенный shell (если установлен django-extensions)
python manage.py shell_plus

# Экспорт данных в JSON
python manage.py dumpdata app.Model --indent 2 > data.json

# Импорт данных из JSON
python manage.py loaddata data.json
```

---

## 🎨 Работа со статикой и медиа
```bash
# Собрать статические файлы
python manage.py collectstatic
```

---

## 🧪 Тестирование
```bash
# Запустить все тесты
python manage.py test

# Запустить тесты конкретного приложения
python manage.py test myapp
```

---

## 🔧 Дополнительно
```bash
# Сбросить пароль суперпользователя (через shell)
python manage.py shell
```
```python
from django.contrib.auth.models import User
u = User.objects.get(username="admin")
u.set_password("newpassword")
u.save()
```

```bash
# Вывести список всех доступных команд
python manage.py help

# Получить помощь по конкретной команде
python manage.py help <command>
```

