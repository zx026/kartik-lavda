from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from ishika.config import MONGO_DB_URI

_client = MongoClient(MONGO_DB_URI, serverSelectionTimeoutMS=5000)
IshikaDB = _client["IshikaChatDB"]

afk = IshikaDB.afk
notes = IshikaDB.notes
filters = IshikaDB.filters
welcome = IshikaDB.welcome
couples = IshikaDB.couples


async def mongoping():
    try:
        _client.admin.command("ping")
        print("[Ishika] MongoDB Connected ✅")
    except ServerSelectionTimeoutError as e:
        print(f"[Ishika] MongoDB Connection Failed ❌ -> {e}")
        raise
