from config import ADMIN_ID
from loader import bot, dp, storage
from middleware import ControlUpdate
import loader
import middleware
import states
import database_schemes
import keyboards
import handlers

async def on_shutdown(dp):
    await bot.close()
    await storage.close()


async def on_startup(dp):
    await bot.send_message(chat_id=ADMIN_ID, text="Raspberry has been started")


if __name__ == "__main__":

    from aiogram import executor

    dp.middleware.setup(ControlUpdate())

    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
