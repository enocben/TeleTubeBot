from typing import List
from pytubefix import Stream
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

from constant import SEPARATOR_DATA_BUTTON
from services import YoutubeDown
from utils import is_youtube_link, format_number, format_bytes


async def get_youtube(url: str) -> YoutubeDown | None:
    try:
        return YoutubeDown(url=url)
    except Exception as e:
        print(f"[ERROR] Failed to create YoutubeDown instance: {e}")
        return None


async def youtube_link_video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.strip()

    if not is_youtube_link(message):
        await update.message.reply_text("❌ Please send a valid YouTube link.")
        return

    loading_msg = await update.message.reply_text("⏳ Loading video info...")

    ytb = await get_youtube(message)

    if ytb is None:
        await loading_msg.delete()
        await update.message.reply_text("⚠️ An error occurred. Please try again later.")
        return

    title = ytb.title or "N/A"
    description = ytb.description or "No description"
    viewers = format_number(ytb.views)
    likes = format_number(ytb.likes)

    buttons_audios = [
        [InlineKeyboardButton(
            f"Audio {format_bytes(stream.filesize)}",
            callback_data=f"{stream.itag}{SEPARATOR_DATA_BUTTON}{message}"
        )]
        for stream in ytb.streams_audio
    ]

    stream_videos: List[Stream] = ytb.streams_video
    buttons_videos = [
        [InlineKeyboardButton(
            f"{stream.resolution}{format_bytes(stream.filesize)}",
            callback_data=f"{stream.itag}{SEPARATOR_DATA_BUTTON}{message}"
        )]
        for stream in stream_videos
    ]

    buttons = buttons_videos + buttons_audios

    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        f"📹 Title: {title}\n"
        f"📝 Description: {description}\n"
        f"👁️ Viewers: {viewers}\n"
        f"❤️ Likes: {likes}",
        reply_markup=reply_markup
    )
    await loading_msg.delete()
