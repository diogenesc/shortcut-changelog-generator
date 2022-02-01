import os
from dotenv import load_dotenv

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

load_dotenv()

dry_run = str2bool(os.environ.get('DRY_RUN', 'false'))
repo_path = os.environ.get('REPO_PATH', './')
api_token = os.environ.get('SHORTCUT_TOKEN')
telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID')
telegram_bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
ignore_last_tag = str2bool(os.environ.get('IGNORE_LAST_TAG', 'false'))
changelog_path = os.environ.get('CHANGELOG_PATH', 'CHANGELOG.md')
telegram_send_diff = str2bool(os.environ.get('TELEGRAM_SEND_DIFF', 'false'))
telegram_title = os.environ.get('TELEGRAM_TITLE')
shortcut_ignore_label = os.environ.get('SHORTCUT_IGNORE_LABEL')