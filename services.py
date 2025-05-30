import os
from pathlib import Path
from typing import List
from pytubefix import YouTube, Stream
from telegram import Update, InputFile
from telegram.ext import CallbackContext


class YoutubeDown:
    def __init__(self, *, url: str):
        self.url = url
        self.ytb = YouTube(self.url,
                           )

    @property
    def title(self) -> str:
        return self.ytb.title

    @property
    def description(self) -> str:
        return self.ytb.description

    @property
    def views(self) -> int:
        return self.ytb.views

    @property
    def likes(self):
        return self.ytb.likes

    @property
    def streams(self) -> List[Stream]:
        return list(self.streams_video + self.streams_audio)

    @property
    def streams_audio(self):
        return list(self.ytb.streams.filter(only_audio=True))

    @property
    def streams_video(self):
        return list(self.ytb.streams.filter(only_video=True, mime_type="video/mp4"))


    async def on_complete_audio(self, update: Update, context: CallbackContext, file_path: str):
        try:
            await context.bot.send_audio(
                chat_id=update.effective_chat.id,
                audio=Path(file_path),
                title=self.title
            )
        finally:
            if Path(file_path).exists():
                os.remove(Path(file_path))

    async def on_complete_video(self, update: Update, context: CallbackContext, file_path: str):
        try:
            await context.bot.send_video(
                chat_id=update.effective_chat.id,
                video=Path(file_path),
                caption=self.title
            )
        finally:
            if Path(file_path).exists():
                os.remove(Path(file_path))