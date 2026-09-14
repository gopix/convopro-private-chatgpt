from pymongo import MongoClient
from pymongo.collection import Collection

from convopro_private_chatgpt.config.settings import settings

_client = MongoClient(settings.MONGO_DB_URL, tz_aware=True)
_db = _client[settings.MONGO_DB_NAME]


def get_collection(name: str) -> Collection:
    """Returns the named collection from the app's MongoDB database."""
    return _db[name]
