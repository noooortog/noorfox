from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["مطور", "مبرمج السورس", "نور"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/3955f6d7c023440c11156.jpg",
        caption="• Dev Bot ↦ المطور \n ━━━━━━━━━━━━ \n • Dev ↦  Cr SoUrce . \n • Bio ↦ 𝗘𝗩𝗘 #𝗥𝗬𝗧𝗛𝗜𝗡𝗚 𝗧𝗛𝗜𝗦 #𝗔𝗖𝗖𝗢𝗨𝗡𝗧 { noordot.t.me } { sw_no.t.me }{ sahnks.t.me }{ vza_o.t.me } { sw_no.t.me }{ vzo_a.t.me } https://t.me/vzo_a",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙲𝚁 𝙽𝙾𝚄𝚁", url=f"https://t.me/nor_o"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Updates", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
