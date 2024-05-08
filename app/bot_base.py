from sqlalchemy import (Integer, String, ForeignKey)
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import relationship, DeclarativeBase, sessionmaker, Mapped, mapped_column
from config import settings


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True)

session_maker = async_sessionmaker(engine,  expire_on_commit=False)


class Base(DeclarativeBase):
    pass

metadata = Base.metadata
class General(Base):
    __tablename__ = 'users'
    index: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    id: Mapped[int] = mapped_column(Integer)  # tg user id
    user_name: Mapped[str] = mapped_column(String(200), nullable=False)
    in_game: Mapped[int] = mapped_column(Integer, default=0)
    secret_number: Mapped[str] = mapped_column(Integer, default=0)
    attempts: Mapped[int] = mapped_column(Integer, default=5)
    total_games: Mapped[int] = mapped_column(Integer, default=0)
    wins: Mapped[int] = mapped_column(Integer, default=0)
    total: Mapped[int] = mapped_column(Integer, default=5)
    game: Mapped[str] = relationship("One_game")


class One_game(Base):
    __tablename__ = 'game'
    index: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    id: Mapped[int] = mapped_column(Integer())
    us_number: Mapped[int] = mapped_column(Integer, nullable=False, unique=False, default=0)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.index'))


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

