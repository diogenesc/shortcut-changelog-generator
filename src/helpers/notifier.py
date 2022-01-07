import os
import helpers.settings as settings
from telegram import Bot
from telegram.utils.helpers import escape_markdown

def telegram(message):
    bot = Bot(settings.telegram_bot_token)

    if settings.telegram_title is not None:
        message = '*' + escape_markdown(settings.telegram_title) + '*' + '\n\n' + message

    bot.send_message(chat_id=settings.telegram_chat_id, text=message, parse_mode='MarkdownV2')