import asyncio
from pyrogram.types import Message
from pyrogram import filters
from Barath import barath, MODULE
import config

@barath.on_message(filters.command(["say"], prefixes=config.HANDLER) & filters.me)
async def say(_, m: Message):
    chat_id = m.chat.id
    cmd = m.command
    text = " ".join(cmd[1:]).strip()
    if len(cmd) < 2:
        await barath.reply_text(f"Provide text.eg {config.HANDLER}.say [text messages]")
        return
    try:
        await m.delete()
    except:
        return
    await barath.send_message(chat_id,text)

@barath.on_message(filters.command(["smsg"], prefixes=config.HANDLER) & filters.me)
async def send_msg(_, m: Message):
    id = int(m.command[1])
    cmd = m.command
    text = " ".join(cmd[2:]).strip()

    if len(cmd) < 2:
        await m.reply_text(f"Use like this: {config.HANDLER}smsg [user/chatid] [text messages]")
        return
    msg =  await m.reply_text("Trying to send msg...")
    
    try:
        await barath.send_message(id,text)
        await msg.edit("Sent Successfully")
    except Exception as err:
        await msg.edit(f"Error Occured!\n{err}")
    try:
        await m.delete()
    except:
        return
    


__mod_name__ = "SPAM"  
    
__help__ = """  
- spam: spam message
- ds: spam with time
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
