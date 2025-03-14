import os
from aiohttp import web
from bot import Bot
from config import TG_BOT_TOKEN, PORT

app = web.Application()

@app.post(f"/{TG_BOT_TOKEN}")
async def webhook_handler(request):
    update = await request.json()
    await Bot.process_update(update)
    return web.Response(text="OK")

async def main():
    await Bot.start()
    print("Bot started!")
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()

Bot.run(main())
