# Kitten App

Kitten App — это веб-приложение на Django, которое предоставляет API для работы с данными о котятах. В проекте используются Django, Django Rest Framework и SQLite как база данных. Приложение запускается в контейнере Docker для удобства развертывания.

## Стек технологий

- Python 3.11
- Django
- Django Rest Framework (DRF)
- SQLite
- Docker

## Установка и запуск

### Шаг 1: Клонирование репозитория

bash
git clone https://github.com/kirsanov69/kittens_app

cd kitten-app

### Шаг 2: Установка зависимостей

pip install -r requirements.txt


### Шаг 3: Миграции базы данных

python manage.py migrate

### Шаг 4: Запуск сервера разработки

python manage.py runserver

### Запуск с Docker
1  Убедитесь, что у вас установлен Docker.
2  Запустите контейнеры с помощью docker-compose:

docker-compose up --build


Приложение будет доступно по адресу: http://127.0.0.1:8000/.

### Работа с API

Kitten App предоставляет API для работы с данными о котятах, такими как их имя, порода, возраст, описание, и т.д. Доступ к API осуществляется через JWT-авторизацию.

### Пример запроса к API для получения списка котят

curl -X GET http://127.0.0.1:8000/api/kittens/ \
     -H "Authorization: Bearer <your-jwt-token>"

### Пример запроса для добавления оценки котенку

curl -X POST http://127.0.0.1:8000/api/kittens/1/rate/ \
     -H "Authorization: Bearer <your-jwt-token>" \
     -H "Content-Type: application/json" \
     -d '{"score": 5}'

### Переменные окружения
DEBUG: Устанавливает режим отладки для Django (1 — включен, 0 — выключен).

### Миграции
Если вы вносите изменения в модели, не забудьте выполнить миграции.

python manage.py makemigrations
python manage.py migrate

### Лицензия
Этот проект распространяется под лицензией MIT. Подробности можно найти в файле LICENSE.


Этот `README.md` охватывает основные шаги для развертывания проекта с использованием Docker и SQLite, а также примеры работы с API.
