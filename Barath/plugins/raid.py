import asyncio
from pyrogram.types import Message
from pyrogram import filters
from Barath import barath, MODULE
import config
import random
from text import TEXT

@barath.on_message(filters.command(["raid"], prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def spam(_, m: Message):
    try:
        reply = m.reply_to_message
        cmd = m.command

        if len(m.command) < 3:
            await barath.send_message(m.chat.id, f"Use like this: `{config.HANDLER}raid [@username] [no. of msg]`")

        else:
            username = cmd[1]
            times = int(cmd[2]) if cmd[2].isdigit() else 10
            
            for x in range(times):
                text = random.choice(TEXT)
                await barath.send_message(
                    m.chat.id,
                    f"{username} {text}"
                )
                await asyncio.sleep(0.10)
    except Exception as e:
        print(e)  # Print the error to the console for debugging purposes


__mod_name__ = "SPAM"  
    
__help__ = """  
- spam: spam message
- ds: spam with time
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
