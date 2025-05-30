import asyncio

from pytubefix import Stream
from telegram import Update
from telegram.ext import CallbackContext

from constant import SEPARATOR_DATA_BUTTON
from services import YoutubeDown
from utils import get_static_files_path


async def get_youtube(url: str) -> YoutubeDown | None:
    try:
        return YoutubeDown(url=url)
    except Exception as e:
        print(f"[ERROR] Failed to create YoutubeDown instance: {e}")
        return None



async def callback_on_press(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer(
        text="Downloading...",
        show_alert=False,
    )

    data = query.data.split(SEPARATOR_DATA_BUTTON)
    tag = data[0]
    url = data[1]


    ytb = await get_youtube(url)

    if ytb is None:
        await query.edit_message_text("⚠️ An error occurred. Please try again later.")
        return

    stream: Stream = ytb.ytb.streams.get_by_itag(tag)

    if not stream:
        return await query.edit_message_text("Stream not found")

    def on_complete(_, file_path):
        if stream.type == "video":
            asyncio.create_task(ytb.on_complete_video(update, context, file_path))
        else:
            asyncio.create_task(ytb.on_complete_audio(update, context, file_path))

    ytb.ytb.register_on_complete_callback(on_complete)

    stream.download(output_path=get_static_files_path())




