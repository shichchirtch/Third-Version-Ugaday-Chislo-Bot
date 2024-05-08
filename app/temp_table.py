from sqlalchemy import MetaData, Table, Column, Integer, text, insert
from bot_base import session_maker, One_game, General
import sqlalchemy as db

# conn = engine.connect()
# metadata = MetaData()
async def INSERT_IN_GAME_TABLE(user_tg_id: int):
    pass
    # async with session_maker() as session:
    #     needed_data = session.query(One_game).filter(One_game.id == user_tg_id).first()
    #     print('needed data = ', needed_data)
    #     #user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.index'))
    #     FK = session.query(General.index).filter(General.id == user_tg_id).scalar()
    #     print('\n\n\nFR  =  ', FK)
    #     if not needed_data:
    #         new_gamer = One_game(id=user_tg_id, us_number=245678, user_id = FK)
    #         session.add(new_gamer)
    #         session.commit()
    #     else:
    #         needed_data.us_number = 0
    #         session.commit()
    # one_game1 = Table('game', metadata,
    #                   Column('index', Integer(), primary_key=True, autoincrement=True),
    #                   Column('id', Integer()),
    #                   Column('us_number', Integer(), nullable=False),
    #                   extend_existing=True)
    # metadata.create_all(engine)
# def insert_user_number_in_one_game_table(table: db.Table, user_tg_id: int, number:int):
#     insertion_query = insert(table).values(id=user_tg_id, us_number=number)
#     conn.execute(insertion_query)
#     conn.commit()
#
#
# def drop_temp_table(table_name: str) -> None:
#     sql = text(f'DROP TABLE IF EXISTS {table_name};')
#     conn.execute(sql)
#     conn.commit()
#
#
# def check_user_number(table: db.Table, nuber_from_message: int):
#     select_query = db.select(table.columns.us_number)
#     select_results = conn.execute(select_query)
#     needed_data_from_first_table = select_results.fetchall()
#     tuple_number = (nuber_from_message,)
#     return tuple_number in needed_data_from_first_table



    # temp_data = db.select(table).where(table.columns.id == user_tg_id)
    # select_all_results = conn.execute(temp_data)
    # needed_data = select_all_results.one_or_none()
    # print('needed_data = ', needed_data)
    # select_query = db.select(table.columns.us_number)
    # select_results = conn.execute(select_query)
    # needed_data_from_game_table = select_results.fetchall()
    # if not needed_data_from_game_table:
    #     print('block if works')
    #     insertion_query = insert(table).values(id=user_tg_id, us_number = 0)
    #     conn.execute(insertion_query)
    #     conn.commit()
    # else:
    #     print('Block else works')
    #     sql = text(f'DROP TABLE IF EXISTS game;')
    #     conn.execute(sql)
    #     conn.commit()
    #     sql = text(f'CREATE TABLE game')
    #     conn.execute(sql)
    #     conn.commit()
    #     one_game1 = Table('game', metadata,
    #                      Column('index', Integer(), primary_key=True, autoincrement=True),
    #                      Column('id', Integer()),
    #                      Column('us_number', Integer(), nullable=False), )
    #     metadata.create_all(engine)
    #     # print('SQL works\n\n\n')
    #     # new_table = text('''
    #     #     CREATE TABLE IF NOT EXISTS game (
    #     #     index INTEGER PRIMARY KEY,
    #     #     id INTEGER NOT NULL,
    #     #     us_number INTEGER NOT NULL)''')
    #     # conn.execute(new_table)
    #     # conn.commit()
#     return one_game1
#
#
# def REFRESH_game_table():
#     print('REFRESH works')
#     # table.drop(engine)
#     sql = text(f'DROP TABLE IF EXISTS game;')
#     conn.execute(sql)
#     conn.commit()
#     print('SQL works\n\n\n')
    # new_table = text('''
    # CREATE TABLE IF NOT EXISTS game (
    # index INTEGER PRIMARY KEY,
    # id INTEGER NOT NULL,
    # us_numer INTEGER NOT NULL)''')
    # conn.execute(new_table)
    # conn.commit()
    # return new_table

    # Table('game', metadata,
    #                  Column('index', Integer(), primary_key=True, autoincrement=True),
    #                  Column('id', Integer()),
    #                  Column('us_number', Integer(), nullable=False), )
    # metadata.create_all(engine)
    # return one_game1

#metadata=MetaData()

# one_game = Table( 'some_name', metadata,
#                      Column('index', Integer(), primary_key=True, autoincrement=True),
#                      Column('id', Integer()),
#                      Column('us_number', Integer(), nullable=False))
# def create_temp_table(user_tg_id: int):
#     """Функция создаёт временную таблицу с названием строквое представление tg_id игрока"""
#     print("\n\nВызвана функция create_temp_table\n\n")
#     one_game = Table(str(user_tg_id), metadata,
#                      Column('index', Integer(), primary_key=True, autoincrement=True),
#                      Column('id', Integer(), default=user_tg_id),
#                      Column('us_number', Integer(), nullable=False), )
#
#     metadata.create_all(engine)
#     return one_game