from pyrogram import Client, filters

@Client.on_message(filters.command("support") & filters.private)
async def support_handler(client, message):
    await message.reply_text("📞 Contact support at: support@example.com")
