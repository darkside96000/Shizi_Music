import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("6027640315:AAE2HyLVZWgM39aYrsJiTEoKXDWon4ATGbI")
BOT_NAME = getenv("Shizi Music")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "alkoreandrama")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("API_ID", "21948417"))
API_HASH = getenv("92e74ed96613e8b552c829713a65f053")
BOT_USERNAME = getenv("@darkside96000_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Fathershab96000")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "friendsforever96000")
PROJECT_NAME = getenv("PROJECT_NAME", "ShiziMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/darkside96000/Shizi_Music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "YWFOYG-UQQWWC-PJSWML-VUEBZH-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
