import logging
import os
from telegram.ext import Application
from bot.config import TELEGRAM_TOKEN
from bot.handlers import register_handlers
from bot.scheduler import start_scheduler
from bot.db import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN is not set! Please check your environment variables.")

    await init_db()

    application = Application.builder().token(TELEGRAM_TOKEN).build()
    register_handlers(application)
    start_scheduler(application)
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

