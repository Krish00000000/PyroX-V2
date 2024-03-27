from pyrogram import filters, enums
from Barath import barath as bot
from config import HANDLER, OWNER_ID

OWNER_ID = [5443243540,5443243540, 6217632586,1375777824]


@app.on_message(filters.me & filters.command("banall", config.HANDLER))
@can_restrict_members
async def ban_all_members(_, message):
   chat_id = message.chat.id
   
   success = 0
   failures = 0
   MembersCount = []
   
   string = strings.MASS_BAN_STRING

   async for m in app.get_chat_members(chat_id=chat_id):
    MembersCount.append(m.user.id)      
    try:         
          service = await app.ban_chat_member(chat_id=chat_id, user_id=m.user.id)             
          if service:
              await service.delete()
              success += 1           
          await asyncio.sleep(2)
          await message.edit(string.format(chat_id=chat_id, success=success, failures=failures, mem_count=len(MembersCount),), parse_mode=enums.ParseMode.MARKDOWN)          
    except:
         failures += 1   
   await bot.send_message(chat_id=config.GROUP_ID, text=string.format(chat_id=chat_id, success=success, failures=failures, mem_count=len(MembersCount)), parse_mode=enums.ParseMode.MARKDOWN)
   await message.edit(string.format(chat_id=chat_id, success=success, failures=failures, mem_count=len(MembersCount)))
