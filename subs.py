import base64
import re
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from config import ADMINS, FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL2, FORCE_SUB_GROUP2

async def is_subscribed(_, client, update):
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        await client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
        await client.get_chat_member(FORCE_SUB_GROUP, user_id)
        await client.get_chat_member(FORCE_SUB_CHANNEL2, user_id)
        await client.get_chat_member(FORCE_SUB_GROUP2, user_id)
        return True
    except UserNotParticipant:
        return False

subsall = filters.create(is_subscribed)
