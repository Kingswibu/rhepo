from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Selamat datang, Saya adalah Asisstant Bot Musik @random_musikkbot.\n\n ❗️ Peraturan:\n   - Tidak boleh spam\n   - Cukup Tambahkan saya ke grup \n\n 👉 **Jika Anda Ingin Mendengarkan Musik Dari Saya**\n\n ⚠️ Info: Jika ada kendala Teknis Atau Kesalahan Dari Bot, Anda Bisa menghubungi @MaafGausahSokap Agar Anda Bisa Mengetahui Masalah bot itu\n    - Jadikan Bot dan Saya Admin di grup Anda.\n   - Jika Anda Limit, Pakai lah akun lain Untuk Menambah kan saya\n\n **FOLLOW IG: @ramadh20**")
  return                        
