from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_NAME = "Ishika"
BOT_USERNAME = "Ishika_chat_bot"

def start_panel():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("📚 Commands", callback_data="help"), InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("📢 Support", url="https://t.me/ishika_support")]
    ])
