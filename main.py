import os
from aiohttp import web
from bot import Bot
from config import TG_BOT_TOKEN, PORT
import pyrogram.utils

# Mengatur MIN_CHANNEL_ID (jika memang perlu)
pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

app = web.Application()

# Handler untuk webhook Telegram
async def webhook_handler(request):
    update = await request.json()
    await Bot().process_update(update)
    return web.Response(text="OK")

# Handler untuk favicon (untuk menghindari error 404)
async def favicon_handler(request):
    return web.Response(status=204)

# Menambahkan route
app.router.add_post(f"/{TG_BOT_TOKEN}", webhook_handler)
app.router.add_get("/favicon.png", favicon_handler)

# Fungsi utama untuk menjalankan bot dan server
async def main():
    await Bot().start()
    print("Bot started!")
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()

# Menjalankan event loop
import asyncio
asyncio.run(main())
