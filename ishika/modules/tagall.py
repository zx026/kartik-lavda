import asyncio
from pyrogram import filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ishika import app

BOT_NAME = "Ishika"
SPAM_CHATS = []

# ========= /TAGALL COMMAND =========
@app.on_message(filters.command(["tagall", "all"]) & filters.group)
async def tag_all(client, message: Message):
    chat_id = message.chat.id

    # Check admin
    admins = [admin.user.id async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    if message.from_user.id not in admins and message.from_user.id!= (await client.get_me()).id:
        return await message.reply("**Sirf Admins tagall use kar sakte hai** ❌")

    if chat_id in SPAM_CHATS:
        return await message.reply("**Pehle se hi tagall chal raha hai**\n**/stop** karke band karo")

    SPAM_CHATS.append(chat_id)

    mention_text = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else f"**{BOT_NAME} calling you** 📢"

    await message.reply(
        f"**{BOT_NAME} TagAll Started** ✅\n\n"
        f"**Message:** {mention_text}\n"
        f"**Stop:** /stop",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⏹️ Stop", callback_data="stop_tagall")]])
    )

    count = 0
    members = [m async for m in client.get_chat_members(chat_id)]

    for member in members:
        if chat_id not in SPAM_CHATS:
            break

        if member.user.is_bot:
            continue

        try:
            count += 1
            mention = f"[{member.user.first_name}](tg://user?id={member.user.id})"

            await client.send_message(
                chat_id,
                f"{mention} {mention_text}",
                disable_web_page_preview=True
            )
            await asyncio.sleep(2) # Spam avoid karne ke liye delay

            if count % 5 == 0:
                await asyncio.sleep(5)

        except Exception:
            pass

    try:
        SPAM_CHATS.remove(chat_id)
    except:
        pass

    await message.reply(f"**{BOT_NAME} TagAll Finished** ✅\n**Total Tagged:** `{count}`")

# ========= /STOP COMMAND =========
@app.on_message(filters.command("stop") & filters.group)
async def stop_tagall(client, message: Message):
    chat_id = message.chat.id

    admins = [admin.user.id async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    if message.from_user.id not in admins:
        return await message.reply("**Sirf Admins stop kar sakte hai** ❌")

    if chat_id in SPAM_CHATS:
        SPAM_CHATS.remove(chat_id)
        await message.reply("**TagAll Stopped Successfully** ⏹️")
    else:
        await message.reply("**Koi TagAll chal hi nahi raha** 😅")

# ========= CALLBACK STOP BUTTON =========
@app.on_callback_query(filters.regex("stop_tagall"))
async def stop_callback(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id

    admins = [admin.user.id async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    if user_id not in admins:
        return await callback_query.answer("**Tum Admin nahi ho** ❌", show_alert=True)

    if chat_id in SPAM_CHATS:
        SPAM_CHATS.remove(chat_id)
        await callback_query.message.edit("**TagAll Stopped by Button** ⏹️")
    else:
        await callback_query.answer("**Already Stopped**", show_alert=True)

# ========= /TAGADMIN COMMAND =========
@app.on_message(filters.command("tagadmins") & filters.group)
async def tag_admins(client, message: Message):
    text = " ".join([admin.user.mention async for admin in client.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)])
    await message.reply(f"**Group Admins:**\n{text}")

# ========= HELP =========
@app.on_message(filters.command("taghelp"))
async def tag_help(client, message: Message):
    await message.reply(
        f"**{BOT_NAME} - TagAll Module**\n\n"
        f"**/tagall <text>** - Sabko mention karke msg bhejo\n"
        f"**/all <text>** - Same as tagall\n"
        f"**/stop** - Tagall ko band karo\n"
        f"**/tagadmins** - Sirf admins ko tag karo\n"
        f"**Example:** `/tagall Meeting hai 5 baje`"
  )
