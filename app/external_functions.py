from bot_base import session_maker, General
from random import randint


async def insert_new_user_in_general_table(user_tg_id: int, name: str):
    pass
    # async with session_maker() as session:
    #     needed_data = session.query(General).filter(General.id == user_tg_id).first()
    #     if not needed_data:
    #         new_us = General(id=user_tg_id, user_name=name)
    #         session.add(new_us)
    #         session.commit()
    #     else:
    #         needed_data.wins = needed_data.total_games = needed_data.secret_number = needed_data.in_game = 0
    #         needed_data.attempts = 5
    #         session.commit()


async def verify_that_user_into_general(user_tg_id: int):
    pass
    # async with session_maker() as session:
    #     needed_data = session.query(General).filter(General.id == user_tg_id).first()
    # return needed_data

#
async def verify_INGAME_status( user_tg_id: int):
    pass
    # async with session_maker() as session:
    #     needed_data = session.query(General.in_game).filter(General.id == user_tg_id).scalar()
    # return needed_data
    # temp_data = db.select(table.columns.in_game).where(table.columns.id == user_tg_id)
    # select_all_results = conn.execute(temp_data)
    # return select_all_results.scalar()
#
#
async def cancel_update(user_tg_id: int):
    pass
    # async with session_maker() as session:
    #     needed_data = session.query(General).filter(General.id == user_tg_id).first()
    #     needed_data.in_game = 0
    #     session.commit()



#     update_query = db.update(table).where(table.columns.id == user_tg_id).values(in_game=0)
#     conn.execute(update_query)
#     conn.commit()
# #
#
async def choosing_number(user_tg_id: int):
    pass
    # async with session_maker() as session:
    #     needed_data = session.query(General).filter(General.id == user_tg_id).first()
    #     needed_data.in_game = 1
    #     needed_data.secret_number=randint(1, 100)
    #     session.commit()

    # update_query = (db.update(table).where(table.columns.id == user_tg_id).values(in_game=1,
    #                                                                               secret_number=randint(1, 100)))
    # conn.execute(update_query)
    # conn.commit()
#
#
# def get_secret_number(table: db.Table, user_tg_id: int):
#     select_query = db.select(table.columns.secret_number).where(table.columns.id == user_tg_id)
#     select_results = conn.execute(select_query)
#     needed_data_from_first_table = select_results.scalar()
#     if needed_data_from_first_table:
#         return needed_data_from_first_table
#     return "This Name Does Not Exist"
#
#
# def update_after_user_wins(table: db.Table, user_tg_id: int):
#     select_query = db.select(table.columns.wins).where(table.columns.id == user_tg_id)
#     select_results = conn.execute(select_query)
#     wins_number = select_results.scalar() + 1
#     select_query = db.select(table.columns.total_games).where(table.columns.id == user_tg_id)
#     select_results = conn.execute(select_query)
#     total_game_number = select_results.scalar() + 1
#     update_query = db.update(table).where(table.columns.id == user_tg_id).values(
#         wins=wins_number, total_games=total_game_number, secret_number=0, in_game=0)
#     conn.execute(update_query)
#     conn.commit()
#
#
# def minus_one_attempt(table: db.Table, user_tg_id: int):
#     select_query = db.select(table.columns.attempts).where(table.columns.id == user_tg_id)
#     select_results = conn.execute(select_query)
#     att_number = select_results.scalar() - 1
#     update_query = db.update(table).where(table.columns.id == user_tg_id).values(attempts=att_number)
#     conn.execute(update_query)
#     conn.commit()
#
#
# def check_attempts_lost_number(table: db.Table, user_tg_id: int):
#     select_query = db.select(table.columns.attempts).where(table.columns.id == user_tg_id)
#     select_results = conn.execute(select_query)
#     att_number = select_results.scalar()
#     if att_number == 0:
#         return True
#     return False
#
#
# def user_lost(table: db.Table, user_tg_id: int):
#     select_query = db.select(table.columns.total_games).where(table.columns.id == user_tg_id)
#     select_results = conn.execute(select_query)
#     total_game_number = select_results.scalar() + 1
#     update_query = db.update(table).where(table.columns.id == user_tg_id).values(
#         total_games=total_game_number, secret_number=0, in_game=0, attempts=5)
#     conn.execute(update_query)
#     conn.commit()
