from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import load_language, get_user_language, add_premium, remove_premium
from db import users_col, premium_col

@Client.on_message(filters.command("admin") & filters.user(123456789))  # Replace with admin ID
async def admin_panel(client, message):
    lang = load_language(get_user_language(message.from_user.id))
    buttons = [
        [InlineKeyboardButton(lang["broadcast"], callback_data="broadcast")],
        [InlineKeyboardButton(lang["view_users"], callback_data="view_users")],
        [InlineKeyboardButton(lang["manage_premium"], callback_data="manage_premium")],
    ]
    await message.reply_text(lang["admin_panel"], reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex("broadcast"))
async def broadcast_handler(client, callback_query):
    lang = load_language(get_user_language(callback_query.from_user.id))
    await callback_query.message.reply_text(lang["broadcast_prompt"])
    response = await client.ask(callback_query.from_user.id, lang["forward_or_copy"])
    forward = response.text.lower() == lang["forward"]

    users = users_col.find({})
    for user in users:
        try:
            if forward:
                await client.forward_messages(user["user_id"], callback_query.message.chat.id, callback_query.message.id)
            else:
                await client.copy_message(user["user_id"], callback_query.message.chat.id, callback_query.message.id)
        except Exception:
            pass

@Client.on_callback_query(filters.regex("view_users"))
async def view_users_handler(client, callback_query):
    count = users_col.count_documents({})
    await callback_query.message.reply_text(f"Total Users: {count}")

@Client.on_callback_query(filters.regex("manage_premium"))
async def manage_premium_handler(client, callback_query):
    buttons = [
        [InlineKeyboardButton("Add Premium", callback_data="add_premium")],
        [InlineKeyboardButton("Remove Premium", callback_data="remove_premium")],
        [InlineKeyboardButton("View Premium Users", callback_data="view_premium")],
    ]
    await callback_query.message.reply_text("Manage Premium Options", reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex("add_premium"))
async def add_premium_handler(client, callback_query):
    user_id = await client.ask(callback_query.from_user.id, "Enter User ID to add Premium:")
    add_premium(int(user_id.text), 30)
    await callback_query.message.reply_text(f"User {user_id.text} added to Premium.")

@Client.on_callback_query(filters.regex("remove_premium"))
async def remove_premium_handler(client, callback_query):
    user_id = await client.ask(callback_query.from_user.id, "Enter User ID to remove Premium:")
    remove_premium(int(user_id.text))
    await callback_query.message.reply_text(f"User {user_id.text} removed from Premium.")

@Client.on_callback_query(filters.regex("view_premium"))
async def view_premium_handler(client, callback_query):
    users = premium_col.find({})
    text = "\n".join([str(user["user_id"]) for user in users])
    await callback_query.message.reply_text(f"Premium Users:\n{text}")
