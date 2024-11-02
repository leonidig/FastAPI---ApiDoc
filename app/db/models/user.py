from sqlalchemy.orm import Mapped, mapped_column

from .. import Base

class User(Base):
    __tablename__ = "users"

    email: Mapped[str]
    password: Mapped[str]
    role: Mapped[str]
