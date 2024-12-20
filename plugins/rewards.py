from pyrogram import Client, filters
from db import users_col
import time

REWARD_TIME = 86400  # 24 hours in seconds

@Client.on_message(filters.command("reward") & filters.private)
async def reward_handler(client, message):
    user = users_col.find_one({"user_id": message.from_user.id})
    if not user:
        users_col.insert_one({"user_id": message.from_user.id, "last_reward": 0})
        user = users_col.find_one({"user_id": message.from_user.id})

    last_reward = user.get("last_reward", 0)
    current_time = time.time()

    if current_time - last_reward >= REWARD_TIME:
        users_col.update_one({"user_id": message.from_user.id}, {"$set": {"last_reward": current_time}})
        await message.reply_text("🎉 You've claimed your daily reward!")
    else:
        remaining_time = REWARD_TIME - (current_time - last_reward)
        hours, minutes = divmod(remaining_time // 60, 60)
        await message.reply_text(f"⏳ Please wait {int(hours)} hours and {int(minutes)} minutes for your next reward.")
