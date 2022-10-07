#Uvindu Bro <https://t.me/UvinduBro>
#😎😍💔💙❤💚💌💥👋✌🤘💻💾📓📗💡📍📌🔓🔒🔐🔏🖇🔗🛡🔮⚘🌷🌱🌲🌟☄☇🌙🌞🌝🌚☈⭐🌟☄
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
👋 Hello [{}](tg://user?id={}),\n\n I'm Emo Song Downloader Bot 🎵

⚘ Just send me the song name you want to download.😋
      eg:```/song Faded```
      
**☇Powerd By </> Emo Bot Devolopers**
**💻 Devoloper** :- @ImRishmika
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="☇ Team Emo", url="https://t.me/EmoBotDevolopers"
                    ),
                    InlineKeyboardButton(
                        text="☄ Support", url="https://t.me/EmoBotSupport"
                    )
                ],
                 InlineKeyboardButton(
                        text="💻 Devoloper", url="https://t.me/ImRishmika"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ Emo Song Bot is online.")
idle()
