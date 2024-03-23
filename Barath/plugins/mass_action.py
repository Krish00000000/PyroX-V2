import config
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from Barath import barath as app

@app.on_message(filters.command("banall", prefixes=config.HANDLER) & filters.me)
async def ban_all_members(_, message: Message):
    x = await app.send_message(message.chat.id, "🖤 Black Magic Started. 🪄")
    try:
        count = 0
        async for user in app.iter_chat_members(message.chat.id):
            if user.status == ChatMemberStatus.MEMBER:
                await app.kick_chat_member(message.chat.id, user.user.id)
                count += 1
        await x.edit_text(f"Banned 🚫 {count} Members.")
    except Exception as e:
        await x.edit_text("Something Went Wrong. Contact Developers loda le le bsdk")

