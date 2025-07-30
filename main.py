from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

import logging
import asyncio
import os

from App.Handlers.handlers import router

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
logging = logging.getLogger(__name__)

async def main():

    load_dotenv()
    token = os.getenv("TOKEN_TG_BOT")
    if not token:
        logging.error("Bot token not found")
        return

    bot = Bot(token)
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)

    try:
        logging.info("Starting the bot...")
        await dp.start_polling(bot)
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped manually")
    except Exception as ex:
        logging.exception(f"Critical error: {ex}")
    finally:
        logging.info("Closing bot session")

if __name__ == "__main__":
    asyncio.run(main())