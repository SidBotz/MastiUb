import os
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from pyrogram.enums import ParseMode

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="plugins"))

if __name__ == "__main__":
    bot.run()
