from aiohttp import web
from pyrogram import Client, filters
from config import TG_BOT_TOKEN, API_HASH, APP_ID

app = web.Application()

bot = Client(
    "bot",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=TG_BOT_TOKEN,
)

@app.route("POST", "/webhook")
async def webhook(request):
    update = await request.json()
    await bot.process_update(update)
    return web.Response(text="OK")

async def main():
    await bot.start()
    print("Bot started!")
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8000)
    await site.start()

bot.run(main())
