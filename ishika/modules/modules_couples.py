from datetime import datetime
import random
from pyrogram import filters
from pyrogram.types import Message
from ishika import app
from ishika.modules.helpers.mongo import couples

BOT_NAME = "Ishika"

@app.on_message(filters.command("couple") & filters.group)
async def couple(client, message: Message):
    chat_id = message.chat.id
    today = datetime.now().strftime("%Y-%m-%d")

    members = [m.user.id async for m in client.get_chat_members(chat_id) if not m.user.is_bot]
    if len(members) < 2: return await message.reply("**Need 2+ members**")

    c1, c2 = random.sample(members, 2)
    c1_u = await client.get_users(c1)
    c2_u = await client.get_users(c2)

    await message.reply(f"**{BOT_NAME} - Today's Couple** 💑\n\n{c1_u.mention} + {c2_u.mention} = ❤️")
