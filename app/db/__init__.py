from sqlalchemy.orm import (sessionmaker,
                            Mapped,
                            mapped_column,
                            DeclarativeBase)
from sqlalchemy import create_engine


ENGINE = create_engine("sqlite:///mydb.db")
SESSION = sessionmaker(bind=ENGINE)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


def up():
    Base.metadata.create_all(ENGINE)


def drop():
    Base.metadata.drop_all(ENGINE)


def migrate():
    drop()
    up()


from .models import Item, User

migrate()