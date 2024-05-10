import asyncio
from aiogram import Bot, Dispatcher
import user_handlers
import command_handlers
from bot_base import init_models
from keyboards import set_main_menu
from bot_tock import BOT_TOKEN

# Функция конфигурирования и запуска бота
async def main():
    await init_models()

    # Инициализируем бот и диспетчер
    bot = Bot(token=BOT_TOKEN,
              parse_mode='HTML')
    dp = Dispatcher()

    # Настраиваем главное меню бота
    await set_main_menu(bot)

    # Регистрируем роутеры в диспетчере
    dp.include_router(command_handlers.command_router)
    dp.include_router(user_handlers.user_router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())