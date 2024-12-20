from pyrogram import Client, filters
from db import analytics_col

@Client.on_message(filters.command("analytics") & filters.user(123456789))  # Replace with admin ID
async def analytics_handler(client, message):
    total_actions = analytics_col.count_documents({})
    await message.reply_text(f"📊 Total Bot Actions: {total_actions}")
