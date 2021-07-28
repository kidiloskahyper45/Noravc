# Lᴜᴄɪᴅᴏ™

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>[🎶](https://telegra.ph/file/7f6694968c6246357aa03.jpg) Welcome {message.from_user.first_name}!
**Nora** is a bot designed for **stream** on your group, as **simple** as possible, through the **voice chats** in your group.

**❓How to use it❓**
Press the » **COMMANDS** to view the full list of the commands of the bot!
and Join [support](https://t.me/unitedbotsupport) to know about this bot 
<\b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "COMMANDS", url="https://telegra.ph/NORA-VC-BOT-07-05",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Support Group", url="https://t.me/rosebakthan"
                    ),
                    InlineKeyboardButton(
                        "Updates Channel", url="https://t.me/rosebakthan"
                    ),
                    InlineKeyboardButton(
                        "Assistant", url="https://t.me/Noravc_assistant"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Add to your group", url="https://t.me/Miss_Monica_bot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Know how to use",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support", url="https://t.me/rosebakthan"
                    ),
                    InlineKeyboardButton(
                        "Report bugs", url="https://t.me/rosebakthan"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "Close", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("source")
    & filters.private
    & ~ filters.edited
)
async def source(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
**Here is bot source code and pyrostring generator For help contact at support group**
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "github repo", url="https://github.com/rosebakthan"
                    ),
                    InlineKeyboardButton(
                        "string generator", url="https://replit.com/@basimon/GMusiqopyrostring"
                    )
                ]
            ]
        )
    )
