import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler

from handlers.callback_on_press import callback_on_press
from handlers.start import start_command
from handlers.youtube import youtube_link_video

load_dotenv()

TOKEN = os.getenv('TOKEN')


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters=None, callback=youtube_link_video))
    # app.add_handler(MessageHandler(filters=None, callback=handle_youtube_link))
    app.add_handler(CallbackQueryHandler(callback_on_press))

    print('Bot is running...')
    app.run_polling()

if __name__ == "__main__":
    main()