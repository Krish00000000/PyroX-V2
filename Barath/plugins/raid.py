import asyncio
import random
from pyrogram.types import Message
from pyrogram import filters
from Barath import barath, MODULE
import config
from text import TEXT

@barath.on_message(filters.command(["raid"], prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def raid(_, m: Message):
    try:
        reply = m.reply_to_message
        cmd = m.command

        if len(cmd) < 3:
            await m.reply_text(f"Use like this: `{config.HANDLER}raid [@username] [no. of msg]`")
            return

        username = cmd[1]
        times = int(cmd[2])

        if not reply:
            await m.delete()
            for x in range(times):
                text = random.choice(TEXT)
                await barath.send_message(
                    m.chat.id,
                    f"{username} {text}"
                )
                await asyncio.sleep(0.10)
        else:
            await m.reply_text("You can't reply to a message while using the raid command.")
    except Exception as e:
        print(e)  # Print the error to the console for debugging purposes


__mod_name__ = "SPAM"  
    
__help__ = """  
- raid: Spam messages mentioning a user with a specified number of messages
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
