import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional

from pymongo import DESCENDING, ReturnDocument

from convopro_private_chatgpt.db.mongo import get_collection

conversations = get_collection("conversations")
conversations.create_index([("last_interacted", DESCENDING)])


# ------ helpers ----------
def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def create_new_conversation_id() -> str:
    return str(uuid.uuid4())


# ----- core services -----
def create_new_conversation(
    title: Optional[str] = None, role: Optional[str] = None, content: Optional[str] = None
) -> str:
    """Creates a new conversation document, optionally seeded with a first message, and returns its id."""
    conv_id = create_new_conversation_id()
    ts = now_utc()
    doc = {
        "_id": conv_id,
        "title": title or "Untitled Conversation",
        "messages": [],
        "last_interacted": ts,
    }
    if role and content:
        doc["messages"].append({"role": role, "content": content, "ts": ts})

    conversations.insert_one(doc)
    return conv_id


def add_message(conv_id: str, role: str, content: str) -> bool:
    """Appends a message to a conversation and bumps last_interacted; returns whether the conversation existed."""
    ts = now_utc()
    res = conversations.update_one(
        {"_id": conv_id},
        {
            "$push": {"messages": {"role": role, "content": content, "ts": ts}},
            "$set": {"last_interacted": ts},
        },
    )
    return res.matched_count == 1


def get_conversation(conv_id: str) -> Optional[Dict[str, Any]]:
    """Fetches a conversation by id, bumping last_interacted as a side effect; None if it doesn't exist."""
    ts = now_utc()
    doc = conversations.find_one_and_update(
        {"_id": conv_id},
        {"$set": {"last_interacted": ts}},
        return_document=ReturnDocument.AFTER,
    )
    return doc


def get_all_conversations() -> Dict[str, str]:
    """Returns {conversation_id: title} for every conversation, most recently interacted with first."""
    cursor = conversations.find({}, {"title": 1}).sort("last_interacted", DESCENDING)
    return {doc["_id"]: doc["title"] for doc in cursor}
