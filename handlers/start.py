from telegram import Update
from telegram.ext import ContextTypes


async def start_command(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome send a link for youtube video")
