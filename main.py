import os
from aiohttp import web
from bot import Bot
from config import TG_BOT_TOKEN, PORT
import pyrogram.utils

# Mengatur MIN_CHANNEL_ID (jika memang perlu)
pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

app = web.Application()

@app.post(f"/{TG_BOT_TOKEN}")
async def webhook_handler(request):
    update = await request.json()
    await Bot().process_update(update)
    return web.Response(text="OK")

async def main():
    await Bot().start()
    print("Bot started!")
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()

# Tidak pakai .run(), gunakan asyncio agar bisa jalan via webhook
import asyncio
asyncio.run(main())
