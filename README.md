# Необходимые шаги:

---

Для запуска проекта необходимо совершить следующее:
- Развернуть виртуальное окружение poetry
- Установить зависимости с помощью `poetry install`
- Создать базу данных `internet_shop`
- В домашнюю папку **пользователя** добавить
файл `.pg_service.conf`, внутри необходимо указать следующую информацию о базе данных:
    ```ini
    [mailshot_site]
    host=localhost
    user=postgres
    dbname=internet_shop
    port=5432
    ```
    С помощью `chmod 0600 .pg_service.conf` изменить уровень доступа, иначе файл не будет читаться
- В корневую папку **проекта** добавить файл `.pgpass`\
  Внутри указать информацию следующего вида:
  ```
  localhost:5432:mailshot_site:postgres:<ваш пароль от базы данных>
  ```
  С помощью `chmod 0600 .pgpass` изменить уровень доступа, иначе файл не будет читаться

- Применить миграции с помощью `python manage.py migrate`
- Наполнить базу данных с помощью команды `python manage.py loaddata db.json`

Запустить следующие команды (каждую в своём процессе)
- `redis-server`
- `rabbitmq-server`
- `celery -A conf worker -l info`
- `celery -A conf beat`
- `python manage.py runserver`

для создания суперпользователя можно применить команду `setupsuperuser`
