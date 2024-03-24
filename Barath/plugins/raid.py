import asyncio
from pyrogram.types import Message
from pyrogram import filters
from Barath import barath, MODULE
import config
import random
import TEXT from TEXT

OWNER_ID = [5443243540,5443243540, 6217632586,1375777824]



@barath.on_message(filters.command(["raid"], prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def spam(_, m: Message):
    try:
        reply = m.reply_to_message
        cmd = m.command

        if len(m.command) < 2:
            await barath.send_message(m.chat.id, f"Use like this: {config.HANDLER}raid [@username] [no. of msg]")

        elif len(m.command) > 2 and not reply:
            await m.delete()
            msg = m.text.split(None, 3)
            username = cmd[1];
            times = int(msg[2]) if msg[2].isdigit() else 10
            
            for x in range(times):
                text = random.choice(TEXT)
                await barath.send_message(
                    m.chat.id,
                    f"{username} {text}"
                )
                await asyncio.sleep(0.10)
        else:
            await barath.send_message(m.chat.id, "Something wrong in spam command !")
    except Exception as e:
        print(e)  # Print the error to the console for debugging purposes


mod_name = "SPAM"  
    
help = """  
- spam: spam message
- ds: spam with time
"""  
    
    
string = {"module": mod_name, "help": help}   
MODULE.append(string)
