import logging
import os
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

# Load variabel lingkungan dari config.env
load_dotenv() 

API_HASH = os.getenv("API_HASH")
APP_ID = int(os.getenv("APP_ID"))
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_BOT_WORKERS = int(os.getenv("TG_BOT_WORKERS", 10))
PORT = int(os.getenv("PORT", 8080))
MONGO_URI = os.getenv("MONGO_URI")

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL")
FORCE_SUB_GROUP = os.getenv("FORCE_SUB_GROUP")
FORCE_SUB_CHANNEL2 = os.getenv("FORCE_SUB_CHANNEL2")
FORCE_SUB_GROUP2 = os.getenv("FORCE_SUB_GROUP2")

LOGGER = print

# Fungsi sederhana untuk mengonversi string ke boolean
def strtobool(val):
    return val.lower() in ("true", "1", "yes")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# API ID dan Hash dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "0"))

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials untuk updater
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Port untuk server
PORT = int(os.environ.get("PORT", "8080"))

# Custom Repo untuk updater
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

# Wajib Subscribe Channel/Group
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_GROUP2 = int(os.environ.get("FORCE_SUB_GROUP2", "0"))

# Jumlah worker bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel tertentu dan pengguna lain bisa mengaksesnya lewat link khusus.</b>",
)

# Admin bot (list User ID)
try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "").split()]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan wajib subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya terlebih dahulu untuk melihat file yang saya bagikan.\n\nSilakan join Channel & Group terlebih dahulu.</b>",
)

# Kustom teks caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Nonaktifkan tombol Bagikan di Channel
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Log file setup
LOG_FILE_NAME = "/tmp/logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.StreamHandler()]
)

RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
[logging.StreamHandler()
]
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Fungsi untuk mendapatkan logger
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
