import asyncio
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bot.db import start_round, reset_round
from bot.config import CHANNEL_URL

emojis = ['🔥', '🌟', '🍀', '🎯', '💎', '🎲', '🧠', '🎉', '🥇', '🚀']

def start_scheduler(app):
    async def emoji_challenge():
        while True:
            await asyncio.sleep(20 * 60)
            for group in app.bot_data.get('groups', []):
                emoji = random.choice(emojis)
                keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Visit Channel", url=CHANNEL_URL)]])
                await start_round(group, emoji)
                await app.bot.send_message(group, f"⚡️ Emoji Challenge! Reply with: {emoji}", reply_markup=keyboard)
                await asyncio.sleep(10)
                await reset_round(group)

    asyncio.create_task(emoji_challenge())
