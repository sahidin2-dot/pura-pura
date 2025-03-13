import os

API_HASH = os.getenv("API_HASH")
APP_ID = int(os.getenv("APP_ID"))
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
PORT = int(os.getenv("PORT", 8000))
