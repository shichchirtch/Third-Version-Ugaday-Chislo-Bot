from aiogram import Router, F
from filters import *
from keyboards import *
from lexicon import positiv_answer, language_dict, negative_answer
from aiogram.types import  Message, ReplyKeyboardRemove, ContentType
from external_functions import (verify_INGAME_status, choosing_number,
                                verify_that_user_into_general,
                                get_secret_number, check_user_previous_schritt,
                                update_after_user_wins, minus_one_attempt,
                                update_game_table, cancel_update, insert_user_number_in_game_table,
                                check_attempts_lost_number)
import time

from bot_base import General



user_router = Router()
@user_router.message(F.content_type != ContentType.TEXT)
async def process_notTEXT_answers(message: Message):
    user_tg_id = message.from_user.id
    user_name = message.chat.first_name
    if await verify_INGAME_status(user_tg_id):
        await message.answer(language_dict['wrong sent data'])
    else:
        await message.answer(user_name + language_dict['wrong content type'])

@user_router.message(DATA_IS_NOT_DIGIT(), F.text.lower().in_(positiv_answer))
async def process_positive_answer(message: Message):
    print("posetive works")
    user_tg_id = message.from_user.id
    await choosing_number(user_tg_id)
    print('choosing_number works')
    await message.answer(text="Я загадал число, начинайте угадывать !",
                         reply_markup=ReplyKeyboardRemove())


# Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
@user_router.message(F.text.lower().in_(negative_answer))
async def process_negative_answer(message: Message):
    user_tg_id = message.from_user.id
    print(f'Юзер ответил нет !')
    if not await verify_INGAME_status(user_tg_id):
        await message.answer(text=language_dict['pity'],
                             reply_markup=keyboard_after_saying_NO)
    else:
        await message.answer(language_dict['wrong sent data'])


@user_router.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    user_tg_id = message.from_user.id
    user_name = message.chat.first_name
    secret_number = await get_secret_number(user_tg_id)
    if await verify_INGAME_status(user_tg_id):
        print('\n\n\ntest chech')
        if int(message.text) == secret_number:
            await update_after_user_wins(user_tg_id)
            await update_game_table(user_tg_id)
            await message.answer(language_dict['wow'] +
                                 user_name +
                                 language_dict['user guessed'] +
                                 str(await get_secret_number(user_tg_id)))
            await message.answer(text=
                                 language_dict['play new game after user wins'],
                                 reply_markup=keyboard1)

        elif int(message.text) > secret_number:
            if await check_user_previous_schritt(user_tg_id, int(message.text)):
                await minus_one_attempt(user_tg_id)
                await insert_user_number_in_game_table(user_tg_id, int(message.text))

                print(f'1 game_list=  \n\n ')

                await message.answer(language_dict['less'])
            else:
                await message.answer(language_dict['dont repeat your number'])

        elif int(message.text) < secret_number:
            if await check_user_previous_schritt(user_tg_id, int(message.text)):
                await minus_one_attempt(user_tg_id)
                await insert_user_number_in_game_table(user_tg_id,  int(message.text))

                print(f'1 game_list=  \n\n ')

                await message.answer(language_dict['more'])
            else:
                await message.answer(language_dict['dont repeat your number'])

        ########################## NO WINNERS,  ATTEMPTS LOST ############################

        if await check_attempts_lost_number(user_tg_id):
            print(f'\n Attempts for {user_name} = 0 Game done !')

            await cancel_update(user_tg_id)
            # await update_game_table(user_tg_id)

            await message.answer(language_dict['unf']+
                                 user_name +
                                 language_dict['no att lost'] +
                                 str(secret_number),
                                 reply_markup=keyboard_after_fail)
            time.sleep(1)

    else:
        await message.answer(text=language_dict['in game false'],
                             reply_markup=keyboard1)


@user_router.message()
async def process_other_answers(message: Message):
    user_tg_id = message.from_user.id
    if not await verify_that_user_into_general(user_tg_id):
        await message.answer(language_dict['start chat'])
    if verify_that_user_into_general(user_tg_id):
        await message.answer(language_dict['wrong sent data'])
    else:
        if message.text == ('/start'):
            await message.answer(language_dict['restart'])
        else:
            await message.answer(language_dict['silly bot'])