import os
from dotenv import load_dotenv
from distutils.util import strtobool

load_dotenv()

dry_run = strtobool(os.environ.get('DRY_RUN', 'false'))
work_dir = os.environ.get('WORK_DIR', '/usr/app')
api_token = os.environ.get('SHORTCUT_TOKEN')
telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID')
telegram_bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
ignore_last_tag = strtobool(os.environ.get('IGNORE_LAST_TAG', 'false'))
changelog_path = os.environ.get('CHANGELOG_PATH', 'CHANGELOG.md')
telegram_send_diff = strtobool(os.environ.get('TELEGRAM_SEND_DIFF', 'false'))