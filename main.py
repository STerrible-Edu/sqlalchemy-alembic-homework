from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import DATABASE_URL
from crud import create_post, create_user, delete_user, get_posts, get_users, update_user


engine = create_engine(DATABASE_URL)


def main():
    email = f"student_{uuid4().hex[:8]}@example.com"

    with Session(engine) as session:
        user = create_user(session, "Иван", email, "Изучаю SQLAlchemy")
        if user is None:
            return

        create_post(session, user.id, "Первый пост", "Проверяю связь OneToMany")
        create_post(session, user.id, "Второй пост", "Проверяю каскадное удаление")

        print("Пользователи:")
        for item in get_users(session):
            print(item.id, item.name, item.email, item.bio)

        print("Посты:")
        for item in get_posts(session):
            print(item.id, item.title, item.user_id)

        update_user(session, user.id, "Иван Петров")
        delete_user(session, user.id)

        print("После удаления пользователя постов осталось:", len(get_posts(session)))


if __name__ == "__main__":
    main()


