### Шаги для запуска

- ## Склонировать репозиторий: git clone https://github.com/dudyaosuplayer/flask.git
- ## Установить зависимости: pip install -r requirements.txt
- ## Создайте файл .env в корне вашего проекта и добавьте необходимые переменные окружения:
    * DB_NAME=your_db_name
    * DB_PORT=your_db_port
    * DB_USER=your_db_user
    * DB_PASS=your_db_pass
    * DB_HOST=your_db_host

- ## Применить миграции для БД: alembic upgrade head
- ## Запуск приложения локально: python app.py
- ## Эндпоинты:
    * для добавления записи: http://127.0.0.1:5000/add
    * для фильтрации(поиска) записей: http://127.0.0.1:5000/search?name=<Example>
  
  



