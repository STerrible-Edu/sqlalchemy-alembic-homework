# Домашнее задание SQLAlchemy ORM и Alembic

Небольшой учебный проект с двумя связанными моделями: `User` и `Post`.
У одного пользователя может быть несколько постов. При удалении пользователя его посты удаляются каскадно.

## Запуск

```bash
docker compose up -d
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
python main.py
```

Строку подключения можно поменять через переменную окружения `DATABASE_URL`.

В папке `migrations/versions` находятся две миграции:

1. Создание таблиц `users` и `posts`.
2. Добавление поля `bio` в модель пользователя.


