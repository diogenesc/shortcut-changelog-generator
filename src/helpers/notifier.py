import os
import helpers.settings as settings
from telegram import Bot

def telegram(message):
    bot = Bot(settings.telegram_bot_token)

    bot.send_message(chat_id=settings.telegram_chat_id, text=message, parse_mode='MarkdownV2')