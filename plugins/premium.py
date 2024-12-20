from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("premium") & filters.private)
async def premium_plans(client, message):
    buttons = [
        [InlineKeyboardButton("1 Month - $5", callback_data="premium_1month")],
        [InlineKeyboardButton("6 Months - $25", callback_data="premium_6months")],
        [InlineKeyboardButton("1 Year - $50", callback_data="premium_1year")],
    ]
    await message.reply_text("💎 Choose a Premium Plan:", reply_markup=InlineKeyboardMarkup(buttons))
