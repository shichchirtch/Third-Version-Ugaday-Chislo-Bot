from sqlalchemy import (Integer, String)
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import sqlite3
import aiogram
engine = create_async_engine("sqlite+aiosqlite:///bot_base2.db", echo=True)

session_maker = async_sessionmaker(engine,  expire_on_commit=False)

class Base(DeclarativeBase):
    pass

metadata = Base.metadata

class General(Base):
    __tablename__ = 'users'
    index: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    id: Mapped[int] = mapped_column(Integer)  # tg user id
    game_nummer: Mapped[int] = mapped_column(Integer, default=0, unique=False)  # uniq number for each game
    user_name: Mapped[str] = mapped_column(String(200), nullable=False)
    in_game: Mapped[int] = mapped_column(Integer, default=0)
    secret_number: Mapped[str] = mapped_column(Integer, default=0)
    attempts: Mapped[int] = mapped_column(Integer, default=5)
    wins: Mapped[int] = mapped_column(Integer, default=0)
    us_number: Mapped[int] = mapped_column(Integer, nullable=False, unique=False, default=0)

class Game(Base):
    __tablename__ = 'game'
    index: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    id: Mapped[int] = mapped_column(Integer)  # tg user id
    att_1: Mapped[int] = mapped_column(Integer, default=0)
    att_2: Mapped[int] = mapped_column(Integer, default=0)
    att_3: Mapped[int] = mapped_column(Integer, default=0)
    att_4: Mapped[int] = mapped_column(Integer, default=0)
    att_5: Mapped[int] = mapped_column(Integer, default=0)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

