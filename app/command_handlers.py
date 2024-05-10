from aiogram import Router
from aiogram.filters import Command, CommandStart
from keyboards import *
from lexicon import start_greeding, language_dict
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove
from external_functions import (insert_new_user_in_general_table, verify_that_user_into_general,
                                verify_INGAME_status, cancel_update, get_user_quantity_games,
                                insert_new_user_in_game_table)

command_router = Router()

@command_router.message(CommandStart())
async def process_start_command(message: Message):
    # Логируем старт Бота
    print(f'user {message.chat.first_name} press start')
    user_name = message.chat.first_name
    user_tg_id = message.from_user.id
    await insert_new_user_in_general_table(user_tg_id, user_name)
    if await get_user_quantity_games(user_tg_id) == 0:
        await insert_new_user_in_game_table(user_tg_id)
        await message.answer(
            f'Привет, {message.chat.first_name} !  \U0001F60A\n {start_greeding}',
                        reply_markup=keyboard1)
    else:
        await message.answer("Запускать меня второй раз бессмыссленно)))",
                             reply_markup=ReplyKeyboardRemove())
    print("Process finfshed")


@command_router.message(Command(commands='help'))
async def process_help_command(message: Message):
    user_tg_id = message.from_user.id
    user_name = message.chat.first_name
    if await verify_that_user_into_general(user_tg_id):
        await message.answer(text=f"{language_dict['game rules']} <b>{user_name}</b> {language_dict['start ?']}",
                             reply_markup=keyboard_for_help)
    else:
        await message.answer('Для начала работы с ботом введите /start',
                             reply_markup=pre_start_clava)


@command_router.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    user_tg_id = message.from_user.id
    if await verify_that_user_into_general(user_tg_id):
        if await verify_INGAME_status(user_tg_id):
            await cancel_update(user_tg_id)
            await message.answer(language_dict['exit from game'],
                                 reply_markup=keyboard_after_saying_NO)
        else:
            await message.answer(text=language_dict['user not in game now'],
                                 reply_markup=keyboard_after_saying_NO)
    else:
        await message.answer(language_dict['if not start'])