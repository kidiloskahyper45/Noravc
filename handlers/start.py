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
        f"""<b>[📻](https://telegra.ph/file/7f6694968c6246357aa03.jpg) Welcome {message.from_user.first_name}!
**musiqo** is a bot designed for **stream** on your group, as **simple** as possible, through the **voice chats** in your group.

**How to use it**
Press the » **COMMANDS** to view the full list of the commands of the bot!
and Join [support](https://t.me/rosebakthan) to know about this bot
<\b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "COMMANDS", url="https://telegra.ph/𝚖𝚞𝚜𝚒𝚚𝚘-Sᴏɴɢ-06-09",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "GROUP", url="https://t.me/rosebakthan"
                    ),
                    InlineKeyboardButton(
                        "CHANNEL", url="https://t.me/rosebakthan"
                    ),
                    InlineKeyboardButton(
                        "CREDITS", url="https://t.me/Musiqorobot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ADD TO GROUPS", url="https://t.me/Noravc_bot?startgroup=true"
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
                        "SUPPORT", url="https://t.me/rosebakthan"
                    ),
                    InlineKeyboardButton(
                        "REPORT BUGS", url="https://t.me/rosebakthan"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "CLOSE", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
Join our group for reporting issues and bugs check commands [click here](https://telegra.ph/𝚖𝚞𝚜𝚒𝚚𝚘-Sᴏɴɢ-06-09) use @missblissrobot for downloading songs
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SOURCE CODE", url="https://github.com/rosebakthan"
                    ),
                    InlineKeyboardButton(
                        "WEBSITE", url="https://telegramorg.com"
                    )
                ]
            ]
        )
    )    

