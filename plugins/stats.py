from pyrogram import Client, filters
from db import users_col, premium_col

@Client.on_message(filters.command("stats") & filters.user(123456789))  # Replace with admin ID
async def detailed_stats(client, message):
    total_users = users_col.count_documents({})
    premium_users = premium_col.count_documents({})
    non_premium_users = total_users - premium_users

    await message.reply_text(
        f"📊 Detailed User Statistics:\n"
        f"👥 Total Users: {total_users}\n"
        f"⭐ Premium Users: {premium_users}\n"
        f"👤 Non-Premium Users: {non_premium_users}"
    )
