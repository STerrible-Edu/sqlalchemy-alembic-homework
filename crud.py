from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from models import Post, User


def create_user(session: Session, name: str, email: str, bio: str | None = None):
    try:
        user = User(name=name, email=email, bio=bio)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except SQLAlchemyError as error:
        session.rollback()
        print(f"Ошибка при добавлении пользователя: {error}")
        return None


def create_post(session: Session, user_id: int, title: str, text: str):
    try:
        post = Post(user_id=user_id, title=title, text=text)
        session.add(post)
        session.commit()
        session.refresh(post)
        return post
    except SQLAlchemyError as error:
        session.rollback()
        print(f"Ошибка при добавлении поста: {error}")
        return None


def get_users(session: Session):
    return session.scalars(select(User).order_by(User.id)).all()


def get_posts(session: Session):
    return session.scalars(select(Post).order_by(Post.id)).all()


def update_user(session: Session, user_id: int, new_name: str):
    try:
        user = session.get(User, user_id)
        if user is None:
            return False
        user.name = new_name
        session.commit()
        return True
    except SQLAlchemyError as error:
        session.rollback()
        print(f"Ошибка при обновлении пользователя: {error}")
        return False


def delete_user(session: Session, user_id: int):
    try:
        user = session.get(User, user_id)
        if user is None:
            return False
        session.delete(user)
        session.commit()
        return True
    except SQLAlchemyError as error:
        session.rollback()
        print(f"Ошибка при удалении пользователя: {error}")
        return False


