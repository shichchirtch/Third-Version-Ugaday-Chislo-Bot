import asyncio
import logging


from aiogram import Bot, Dispatcher
import user_handlers
import command_handlers
from bot_base import init_models

from keyboards import set_main_menu


# Функция конфигурирования и запуска бота
async def main():
    await init_models()
    # Конфигурируем логирование
    # logging.basicConfig(
    #     level=logging.INFO,
    #     format='%(filename)s:%(lineno)d #%(levelname)-8s '
    #            '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    # logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    # config: Config = load_config()



    # Инициализируем бот и диспетчер
    bot = Bot(token="6850109769:AAF7H94Jn5TmMhPQwmDqgXId2Ik_MQT4sIM",
              parse_mode='HTML')
    dp = Dispatcher()

    # Настраиваем главное меню бота
    await set_main_menu(bot)

    # Регистрируем роутеры в диспетчере
    dp.include_router(command_handlers.command_router)
    dp.include_router(user_handlers.user_router)
    # metadata.drop_all(engine)



    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




asyncio.run(main())