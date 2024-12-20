from pyrogram import Client, filters

@Client.on_message(filters.command("status") & filters.user(123456789))  # Replace with admin ID
async def bot_status(client, message):
    await message.reply_text("✅ Bot is running and online.")
