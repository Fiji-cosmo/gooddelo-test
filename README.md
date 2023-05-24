# gooddelo-test
Тестовое задание для Gooddelo

# Запуск проект
Для запуска проект нужно клонировать репозиторий к себе на пк ```git clone git@github.com:Fiji-cosmo/gooddelo-test.git```

Далее создать виртуальное окружение ```py -3.11 -m venv venv``` и активировать его ```source venv/Scripts/activate```

Создать файл .env в корне проекта
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=aramud
DB_HOST=db
DB_PORT=5432
SECRET_KEY='django-insecure-t1xz-o6f_eb3n=x&s%c^1nqrk2a7w84q__reoy1!y!n1-8=uvc'
```

После этого собрать образы в контейнер командой ```docker-compose up -d --buil```

Сделать миграции ```docker-compose exec web python manage.py migrate```

Собрать статику ```docker-compose exec web python manage.py collectstatic --no-input```

Создать суперюзера для вохода в админку ```docker-compose exec web python manage.py createsuperuser```

# Доступные эндпоинты
http://localhost/api/register/ - регистрация нового пользователя

http://localhost/api/tasks/ - при GET запросе будет получен список всех записей, при POST запросе будет создана новая запись

http://localhost/api/tasks/<int:pk>/ - GET запрос выведет конкретную запись по её id, так же создатель записи может изменять (PUT запрос) или удалить свою запись (DELETE)

http://localhost/api/auth/login/ - POST запрос на получение JWT токена для работы с API

http://localhost/api/auth/logout/ - POST запрос для выхода из своего профиля 

http://localhost/api/auth/refresh_token/ - POST запрос для обновления устаревшего JWT токена на новый.

# Автор
Илья Ховрин

# Стек
python - django - postgreSQL - SimpleJWT - Docker
