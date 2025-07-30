from telegram import Update
from telegram.ext import ContextTypes
from bot.db import get_leaderboard

async def show_leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    group_id = update.effective_chat.id
    leaderboard = await get_leaderboard(group_id)

    if not leaderboard:
        await update.message.reply_text("No scores yet!")
        return

    text = "🏆 Group Leaderboard 🏆\n\n"
    for i, user in enumerate(leaderboard, 1):
        text += f"{i}. {user.get('username', 'Unknown')} — {user['score']} points\n"

    await update.message.reply_text(text)
