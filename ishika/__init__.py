import logging

from pyrogram import Client

from ishika.config import API_ID, API_HASH, BOT_TOKEN

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

LOGGER = logging.getLogger("Ishika")

app = Client(
    "IshikaBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="ishika/modules"),
)
