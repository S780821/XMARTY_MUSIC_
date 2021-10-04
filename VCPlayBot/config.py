import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Xmarty_Support")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/3aa55e7efe0fabf05da4e.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XmartyAssistant")
OWNER_NAME = getenv("OWNER_NAME", "Xmartperson")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Xmarty_Support")
PROJECT_NAME = getenv("PROJECT_NAME", "Xmartybot2")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/S780821/Xmarty_Music_2")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1914050048").split()))
