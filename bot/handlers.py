from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes
from bot.leaderboard import show_leaderboard
from bot.db import get_round, increment_score, set_winner
from bot.config import CHANNEL_URL

def register_handlers(app):
    app.add_handler(CommandHandler('leaderboard', show_leaderboard))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_chat or not update.effective_user:
        return

    group_id = update.effective_chat.id
    user = update.effective_user
    text = update.message.text

    round_info = await get_round(group_id)
    if round_info and round_info.get('active') and round_info.get('winner') is None:
        if text.strip() == round_info['emoji']:
            await increment_score(group_id, user.id, user.username or user.first_name)
            await set_winner(group_id, user.id)
            await update.effective_chat.send_message(
                f"🎉 {user.mention_html()} won the round with {text}!",
                parse_mode='HTML'
            )
