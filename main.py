import os
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

app = Client(
    "music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text("أهلاً بك! بوت الموسيقى الخفيف يعمل بنجاح ومستعد للعمل.")

print("Bot is starting...")
app.run()
