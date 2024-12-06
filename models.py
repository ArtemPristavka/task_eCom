from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column
)
from sqlalchemy import Text


class Base(DeclarativeBase):
    pass


class Template(Base):
    __tablename__ = "template"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text())
    template: Mapped[str]
