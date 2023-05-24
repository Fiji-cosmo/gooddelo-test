# gooddelo-test
Тестовое задание для Gooddelo

# Запуск проект
Для запуска проект нужно клонировать репозиторий к себе на пк git clone git@github.com:Fiji-cosmo/gooddelo-test.git.

Далее создать и активировать виртуальное окружение py -3.11 -m venv venv и активировать его source venv/Scripts/activate

После этого собрать образы в контейнер командой docker-compose up -d --buil

Сделать миграции docker-compose exec web python manage.py migrate

Собрать статику docker-compose exec web python manage.py collectstatic --no-input 

Создать суперюзера для вохода в админку docker-compose exec web python manage.py createsuperuser

# Доступные эндпоинты
api/register/ - регистрация нового пользователя

api/tasks/ - при GET запросе будет получен список всех записей, при POST запросе будет создана новая запись

api/tasks/<int:pk>/ - GET запрос выведет конкретную запись по её id, так же создатель записи может изменять (PUT запрос) или удалить свою запись (DELETE)

api/auth/login/ - POST запрос на получение JWT токена для работы с API

api/auth/logout/ - POST запрос для выхода из своего профиля 

api/auth/refresh_token/ - POST запрос для обновления устаревшего JWT токена на новый.

# Автор
Илья Ховрин

# Стек
python - django - postgreSQL - SimpleJWT - Docker
