from Barath import barath as app
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus

pbot = app
x = await message.reply_text("🖤 Black Magic Started. 🪄")
await message.delete()  # Change msg to message
try:
    count = 0
    async for users in app.get_chat_members(message.chat.id):  # Change msg to message
        if users.status == ChatMemberStatus.MEMBER:
            await app.ban_chat_member(message.chat.id, users.user.id)
            count += 1
    await x.edit_text(f"Banned 🚫 {count} Members.")
except Exception:
    await x.edit_text("Something Went Wrong. Contact Developers loda le le bsdk")
