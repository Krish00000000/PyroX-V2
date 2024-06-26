import requests
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ChatType, ChatAction
from Barath import barath as pbot
from Barath.plugins.alive import ping

BOT_NAME = "Leena"
OWNER = "@UnknownTFG"


fixed_responses = {
    "who made you": "I was made by my creator @Ikaris0_0",
    "who are you": "I am a chatbot created by my owner :- @UnknownTFG",
    "what is ping of server": "The current server ping is {} milliseconds, And Uptime Of Service is {}.",
    "what is your name": "My name is Leena",
    "who is your owner": "My owner is @UnknownTFG"
}

CHAT = {}

@pbot.on_message(filters.command("chat", prefixes=".") & filters.me)
async def toggle_chat(_, message: Message):
    try:
        status = message.command[1].lower()
        if status == "on":
            CHAT[message.chat.id] = True
            await message.reply_text("ChatBot enabled for this chat.")
        elif status == "off":
            CHAT[message.chat.id] = False
            await message.reply_text("ChatBot disabled for this chat.")
        else:
            await message.reply_text("Invalid command usage. Use .chat on or .chat off.")
    except IndexError:
        await message.reply_text("Invalid command usage. Use .chat on or .chat off.")

@pbot.on_message(filters.text & ~filters.me & filters.reply)
async def chatbot(_, message: Message):
    if message.chat.id not in CHAT or not CHAT[message.chat.id]:
        return
    if message.chat.type != ChatType.SUPERGROUP:
        if not message.reply_to_message:
            return
        elif message.reply_to_message.from_user.id != (await pbot.get_me()).id:
            return

    if message.text and message.text[0] in ["/", "!", "?", "."]:
        return
        
    replied_user_id = message.reply_to_message.from_user.id
    if replied_user_id == 6217632586:
        await pbot.send_chat_action(message.chat.id, ChatAction.TYPING)
        
        response_text = fixed_responses.get(message.text.lower(), None)
        if response_text:
            if "{}" in response_text:
                server_ping, server_uptime = await ping_pong()
                response_text = response_text.format(server_ping, server_uptime)
            await message.reply_text(response_text)
        else:
            # If not
            response = requests.get(f"https://apis-tofu.koyeb.app/api/chatbot/{BOT_NAME}/{OWNER}/{message.text}")

            if response.status_code == 200:
                try:
                    results = response.json()
                    await message.reply_text(results.get("reply", "No reply from the chatbot."))
                except json.JSONDecodeError:
                    await message.reply_text("Failed to decode the chatbot response.")
            elif response.status_code == 429:
                await message.reply_text("ChatBot Error: Too many requests. Please wait a few moments.")
            elif response.status_code >= 500:
                await message.reply_text("ChatBot Error: API server error. Contact us at @UnknownTFG.")
            else:
                await message.reply_text("ChatBot Error: Unknown Error Occurred. Contact us at @UnknownTFG.")
