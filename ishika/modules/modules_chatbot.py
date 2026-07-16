from pyrogram import filters, enums
from pyrogram.types import Message

from ishika import app, LOGGER
from ishika.config import BOT_USERNAME
from ishika.modules.helpers.gemini import ask_gemini

# Commands handled elsewhere - the chatbot should never intercept these
KNOWN_COMMANDS = ["start", "tagall", "all", "stop", "tagadmins", "taghelp", "couple"]


async def replied_to_bot(_, client, message: Message) -> bool:
    return bool(
        message.reply_to_message
        and message.reply_to_message.from_user
        and client.me
        and message.reply_to_message.from_user.id == client.me.id
    )


REPLIED_TO_BOT = filters.create(replied_to_bot)

CHATBOT_FILTER = (
    filters.text
    & ~filters.via_bot
    & ~filters.command(KNOWN_COMMANDS)
    & (filters.private | filters.mentioned | REPLIED_TO_BOT)
)


@app.on_message(CHATBOT_FILTER)
async def chatbot_reply(client, message: Message):
    prompt = message.text or ""

    if BOT_USERNAME:
        prompt = prompt.replace(f"@{BOT_USERNAME}", "").strip()

    if not prompt:
        return

    await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)

    try:
        reply = await ask_gemini(prompt)
    except Exception as e:
        LOGGER.error(f"Gemini error: {e}")
        reply = "Abhi thodi dikkat aa rahi hai, thodi der baad try karo 🙏"

    await message.reply(reply)
