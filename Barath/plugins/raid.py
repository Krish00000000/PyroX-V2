import asyncio
from pyrogram.types import Message
from pyrogram import filters
from Barath import barath, MODULE
import config
import random

# Devs ya authorized users ki IDs dalen
DEVS = [5443243540, 6217632586, 1375777824]

TEXT = [
    # Yahaan text messages daalen
]

# Raid command ko sirf authorized users ka upyog karne dena
@barath.on_message(filters.command(["raid"], prefixes=config.HANDLER) & filters.user(DEVS))
async def spam(_, m: Message):
    try:
        reply = m.reply_to_message
        cmd = m.command

        if len(m.command) < 2:
            await barath.send_message(m.chat.id, f"Use like this: `{config.HANDLER}raid [@username] [no. of msg]`")

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

# Module ka naam aur help information
__mod_name__ = "SPAM"  
__help__ = """  
- spam: spam message
- ds: spam with time
"""  
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string) 
