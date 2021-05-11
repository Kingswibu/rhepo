from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Jadikan Saya Sebagai Admin Di grup Anda.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "RANDOM MUSIK"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Saya Bergabung di Grup anda")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>@asistan_random Suda Siap Dalam Chat</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your group due to heavy join requests for userbot! Make sure user is not banned in group."
            "\n\nOr Undang secara manual  @asistan_random Ke grup Anda sekai lagi</b>",
        )
        return
    await message.reply_text(
            "<b>@asistan_random userbot Telah Bergabung Di Grup Anda</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Saya Keluar Dari Grup anda, Mungkin Karna sudah Terlalu banyak Pemakaian."
            "\n\nOr Keluarkan Saya Secara Manual</b>",
        )
        return
