import asyncio
from pyrogram.types import Message
from pyrogram import filters
from Barath import barath, MODULE
import config
import random

# Devs ya authorized users ki IDs dalen
DEVS = [5443243540, 6217632586, 1375777824]

TEXT = ["Teri ma ka bhosda sale maderchod ki aulad 🤬",

"GAND KII DHAAR BHOSDIKE FATEE HUE CONDOM KI NAAJAIS PAIDAISH",

"Teri maa ki choot gand kay tatto teri maa ka bhosda karke uski gaand mai ping pong kar dunga",

"Phatele Nirodh Ke Natije! 😂😂",

"Teri Gaand Mein Kutte Ka Lund 🖕 Teri Jhaatein Kaat Kar Tere Mooh Par Laga Kar Unki French Beard Bana Doonga!",

"chut kay baal nipple ki dhaar teri gaand mai Road roller de dunga 🖕🤬",

"Chullu Bhar Muth Mein Doob Mar Kaali Chut Ke Safed Jhaat",

"chutiye behenchod lauda madarchod gaandu bhosadikey",

"Gote Kitne Bhi Badey Ho, Lund Ke Niche Hi Rehtein Hain",

"Chipkali ki bhigi chut Choot kay baal Chipkali ke jhaat ke paseene",

"madar chod bhosdke esa lagta h apne hii taaate kaat ke chipka diya apni shakal dekh lodee jese shakal aur gand me h aakal",

"Teri ma ki gand me hathi ka lund dalke asa chodunga Na Bacha hojayega Johny sins ,ke lund se chudwaungu bhosdike",

"14 baap ki Najais olad randi kay beez chinnale",

"GAND MAI VIMAL KI GOLI BNA KAR DE DUNGA BHENCHO TERI GAAND MAI RAILWAY STATION KA FATAK DE DUNGA 😂😂🤬🖕",

"teri maa k bhosde mai MDH CHANA MASALA daal k tere baap ko vo spicy bhosda khila dunga 🥵🤮",

"SALA TARI BHAN KO ROAD PA LAJA KA KA NANGA KAR KA BAACHO SA CHUD VAU",

"teri ma Randi tera baap hizda kaali gaand kay Khade baal jhaatu Randi kay chodu",

"TERA BAAP JOHNY SINS CIRCUS KAY BHOSDE JOKER KI CHIDAAS 14 LUND KI DHAAR TERI MUMMY KI CHUT MAI 200 INCH KA LUND",

"maa k lode tere jese randi k baccho ko bachpan mai maar dena chiye",

"madarchod chutmarke teri tatti jesi shakl pe pad dunga bhen k lode chutiye",

"Bhenchod baap se panga matt le Warna maa chodh di Jayegi 🤬","Bhosdike madarchod bhen k lode maachar ki jhaat gandu maa ki chut", "teri tatto ke soudagaR  ",
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
