import asyncio
import random
from pyrogram.types import Message
from pyrogram import filters
from Barath import barath, MODULE
import config


TEXT = [
"Bhosdike madarchod bhen k lode maachar ki jhaat gandu maa ki chut", "teri tatto ke soudagaR  ",
"hijde ki aulad",
"Kutte ke poot, teri maa ki choot Lavde ke bal Lund Chus Lundoos",
"Lund Ke Pasine",
"Meri Gand Ka Khatmal",
"Najayaz paidaish",
"Rundi khana",
"Sadi hui gaand",
"Teri gaand main kute ka lund",
"Teri maa ka bhosda",
"Teri maa ki chut",
"Tere gaand mein keede paday",
"Ullu ke pathe",
"Phatele Nirodh Ke Natije! Chut Ka Maindak…Abla Naari, Tere Bable", "Bhaari… Chut Ke Pasine Mein Talay Hue Bhajiye…Chullu Bhar Muth Mein Doob Mar! Kaali Chut Ke Safed Jhaant…Gote Kitne Bhi Badey Ho, Lund Ke Niche Hi Rehtein Hain…Naa Chut, Naa Choche, Aur Nakhre Noor Jahan Ke!Teri Gaand Mein Kutte Ka Lund…Teri Jhaatein Kaat Kar Tere Mooh Par Laga Kar Unki French BeardBanaDoonga! Maderchod-Bhosadike-Bhen chodBeti chod",
"BhadhavaChoduGaandGaanduGadha, BaklandLauda, Lund Hijra KuttiyaPaad", "Randi Saala kutta Saali kutti TattiKamina",
"Chut ke pasine mein talay huye bhajiye- Snack fried in pussy sweat Chut", "ke dhakkan Chut ke gulam Chutiya ka bheja ghas khane gaya ha Choot", "marani ka",
"Choot ka baal Chipkali ke jhaat ke baal",
"Chipkali ke jhaat ke paseene Chipkali ke gaand ke pasine Chipkali ke", "chut ke pasine Chipkali ki bhigi chut Chinaal ke gadde ke nipple ke", "baal ke joon Chullu bhar muth mein doob mar Cuntmama",
"Chhed Apni gaand mein muthi daal",
"Apni lund choos Apni ma ko ja choos",
"Bhen ke laude Bhen ke takke Abla naari tera buble bhaari", "Bhonsri-Waalaa- You fucker Bhadwe ka awlat Bhains ki aulad Buddha paad Bol teri gand kaise maru",
"Bur ki chatani Chunni Chinaal",
"Chudai khana Jhaant ke pissu Kadak Mall Kali Choot Ke Safaid Jhaat",
"Khotey ki aulda Kutte ka awlat Kutte ki jat Kutte ke tatte Kutte ke poot, teri maa ki choot", 
"Lavde ke bal Lund Chus Lundoos Lund Ke Pasine- Meri Gand Ka Khatmal Moot, Mootna Najayaz paidaish",
"Goll chuchi Pink Choot Laal Gand = Teri Behane (aaye Haaye)",
"Ftti Hue choot Brown Gaand Lamke Hue Mummee = Teri Mummy"
  "gandu"
]


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
