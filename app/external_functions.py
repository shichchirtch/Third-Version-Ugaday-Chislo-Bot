from bot_base import session_maker, General, Game
from random import randint
from sqlalchemy import select

async def insert_new_user_in_game_table(user_tg_id: int):
    async with session_maker() as session:
        query = await session.execute(select(Game).filter(Game.id == user_tg_id))
        needed_data = query.scalar()
        print('needed_dataGAME = ', needed_data)
        new_us = Game(id=user_tg_id)
        session.add(new_us)
        await session.commit()

async def insert_new_user_in_general_table(user_tg_id: int, name: str):
    print('user_tg_id =', user_tg_id)
    async with session_maker() as session:
        query = await session.execute(select(General).filter(General.id == user_tg_id))
        print('query =', query)
        needed_data = query.scalar()
        print('needed_data = ', needed_data)
        if not needed_data:
            new_us = General(id=user_tg_id, user_name=name)
            session.add(new_us)
            await session.commit()
        else:
            print('else works')
            print('needed_data = ', needed_data.user_name)
            needed_data.secret_number = needed_data.in_game = 0
            needed_data.attempts = 5
            needed_data.game_nummer += 1
            await session.commit()

async def get_user_quantity_games(user_tg_id: int):
    '''Функция не позволяет выводить стартовое приветсвие повторно'''
    async with session_maker() as session:
        query = await session.execute(select(General).filter(General.id == user_tg_id))
        needed_data = query.scalar()
        return needed_data.game_nummer


async def verify_that_user_into_general(user_tg_id: int):
    '''Функция не позволяет выводить читать правила до старта бота'''
    async with session_maker() as session:
        query = await session.execute(select(General).filter(General.id == user_tg_id))
        needed_data = query.scalar()
        return needed_data

async def verify_INGAME_status( user_tg_id: int):
    '''Функция проверяет в игре юзер или нет'''
    async with session_maker() as session:
        query = await session.execute(select(General).filter(General.id == user_tg_id))
        needed_data = query.scalar()
        return needed_data.in_game

async def cancel_update(user_tg_id: int):
    '''Функция выводит юзера из игры'''
    async with session_maker() as session:
        query = await session.execute(select(General).filter(General.id == user_tg_id))
        needed_data = query.scalar()
        needed_data.in_game = 0
        needed_data.attempts = 5
        needed_data.game_nummer += 1
        await session.commit()
        query_game = await session.execute(select(Game).filter(Game.id == user_tg_id))
        n = query_game.scalar()
        n.att_1 = n.att_2 = n.att_3 = n.att_4 = n.att_5 = 0
        await session.commit()

async def choosing_number(user_tg_id: int):
    '''Функция выводит юзера из игры'''
    async with session_maker() as session:
        query = await session.execute(select(General).filter(General.id == user_tg_id))
        needed_data = query.scalar()
        needed_data.in_game = 1
        needed_data.attempts = 5
        needed_data.game_nummer += 1
        needed_data.secret_number = randint(1, 100)
        await session.commit()


async def get_secret_number(user_tg_id: int):
    '''Функция записывает в область видимости хэндлера загаданное ботом число для данного юзера'''
    async with session_maker() as session:
        query = await session.execute(select(General).filter(General.id == user_tg_id))
        needed_data = query.scalar()
        return needed_data.secret_number


async def check_user_previous_schritt(user_tg_id:int, new_number:int):
    '''Функция проверяет поля att1-5 таблицы Game на отсутствие совпалений'''
    async with session_maker() as session:
        query = await session.execute(select(Game).filter(Game.id == user_tg_id))
        n = query.scalar()
        if new_number not in (n.att_1, n.att_2, n.att_3, n.att_4, n.att_5):
            return True
        return False


async def update_after_user_wins(user_tg_id: int):
    '''Функция обновляет таблицу users после победы'''
    async with session_maker() as session:
        query = await session.execute(select(General).filter(General.id == user_tg_id))
        needed_data = query.scalar()
        needed_data.in_game = 0
        needed_data.attempts = 5
        needed_data.game_nummer += 1
        needed_data.wins += 1
        await session.commit()

async def update_game_table(user_tg_id:int):
    '''Функция обновляет таблицу game'''
    async with session_maker() as session:
        query = await session.execute(select(Game).filter(Game.id == user_tg_id))
        n = query.scalar()
        n.att_1 = n.att_2 = n.att_3 = n.att_4 = n.att_5 = 0
        await session.commit()

async def insert_user_number_in_game_table(user_tg_id:int, us_number:int):
    '''Функция обновляет таблицу game'''
    async with session_maker() as session:
        query = await session.execute(select(Game).filter(Game.id == user_tg_id))
        n = query.scalar()
        if n.att_1 == 0:
            n.att_1 = us_number
        elif n.att_2 == 0:
            n.att_2 = us_number
        elif n.att_3 == 0:
            n.att_3 = us_number
        elif n.att_4 == 0:
            n.att_4 = us_number
        elif n.att_5 == 0:
            n.att_5 = us_number
        await session.commit()


async def minus_one_attempt(user_tg_id: int):
    '''Функция уменьшает количество попыток'''
    async with session_maker() as session:
        query = await session.execute(select(General).filter(General.id == user_tg_id))
        needed_data = query.scalar()
        needed_data.attempts -= 1
        await session.commit()


async def check_attempts_lost_number(user_tg_id: int):
    '''Функция проверяет остались ли попытки у юзера'''
    async with session_maker() as session:
        query = await session.execute(select(General).filter(General.id == user_tg_id))
        needed_data = query.scalar()
        print('\n\n\nneeded_data.attempts', needed_data.attempts)
        if needed_data.attempts == 0:
            return True
        return False

