from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAx0CVij2LgABEzNHYK73j8kBtxw0_SoHsMzUQ5gEu6MAAn4MAAJLae4QXlcTPAtFOZsfBA")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nSaya Adalah Bot yang akan memainkan Musik Di VCG Group Anda
Saya di Buat Oleh [RAMA](https://t.me/maafgausahsokap) ❤
\nJangan Lupa Follow IG creator saya @ramadh20 😍
\nHit /help list of available commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "OWNER", url="https://t.me/MaafGausahSokap",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/teman_random"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/ramubotinfo"
                    ),
                    InlineKeyboardButton(
                        "MY ASISTANT", url="https://t.me/random_asisstan"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Random_musikkbot?startgroup=true"
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
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel info", url="https://t.me/ramubotinfo"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
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
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/candu_musikk"
                    )
                ]
            ]
        )
    )    
