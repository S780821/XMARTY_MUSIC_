
import logging
from time import time
from datetime import datetime
from VCPlayBot.config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, SUPPORT_GROUP
from VCPlayBot.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from VCPlayBot.helpers.decorators import sudo_users_only

logging.basicConfig(level=logging.INFO)

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ **𝙒𝙀𝙇𝘾𝙊𝙈𝙀 {message.from_user.first_name}** \n
💭 ****[{BOT_NAME}](https://t.me/{BOT_USERNAME})] αℓℓοω γου το ρℓαγ мυѕιϲ οи gяουρѕ τняουgн τнє иєω τєℓєgяαм'ѕ νοιϲє ϲнατѕ!**

💡 **ƒιи∂ ουτ οƒ αℓℓ τнє ϐοτ'ѕ ϲοммиα∂ѕ αи∂ нοω τнєγ ωοяκ ϐγ ϲℓιϲκιиg οи τнє ϲοммαи∂ѕ ϐυττοи !**

❓ **𝗙𝗼𝗿 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗮𝗯𝗼𝘂𝘁 𝗮𝗹𝗹 𝗳𝗲𝗮𝘁𝘂𝗿𝗲 𝗼𝗳 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁, 𝗷𝘂𝘀𝘁 𝘁𝘆𝗽𝗲 /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ α∂∂ мє το γουя gяουρ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "🤔 ɦσω ƭσ µรε ɱε", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "🗡️ ϲοммαи∂ѕ", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "💸 ∂οиατє", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "😈 οƒƒιϲιαℓ gяουρ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "👉 οƒƒιϲιαℓ ϲнαииєℓ", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "✨ мακє υя οωи ϐοτ ✨", url="https://github.com/S780821/Xmarty_Music_2"

                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ**\n<b>💠 **ᴜᴘᴛɪᴍᴇ:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ Group", url=f"https://t.me/Xmarty_Support"
                    ),
                    InlineKeyboardButton(
                        "✨ мακє υя οωи ϐοτ ✨", url="https://github.com/S780821/Xmarty_Music_2"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **𝙃𝙀𝙇𝙇𝙊** {message.from_user.mention()}</b>

**𝑷𝒍𝒆𝒂𝒔𝒆 𝒑𝒓𝒆𝒔𝒔 𝒕𝒉𝒆 𝒃𝒖𝒕𝒕𝒐𝒏 𝒃𝒆𝒍𝒐𝒘 𝒕𝒐 𝒓𝒆𝒂𝒅 𝒕𝒉𝒆 𝒆𝒙𝒑𝒍𝒂𝒏𝒂𝒕𝒊𝒐𝒏 𝒂𝒏𝒅 𝒔𝒆𝒆 𝒕𝒉𝒆 𝒍𝒊𝒔𝒕 𝒐𝒇 𝒂𝒗𝒂𝒊𝒍𝒂𝒃𝒍𝒆 𝒄𝒐𝒎𝒎𝒂𝒏𝒅𝒔 !**

⚡ __Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❔ HOW TO USE ME", callback_data="cbguide"
                    )
                ]
            ]
        ),
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>💡 𝙃𝙀𝙇𝙇𝙊 {message.from_user.mention} 𝖜𝖊𝖑𝖈𝖔𝖒𝖊 𝖙𝖔 𝖙𝖍𝖊 𝖍𝖊𝖑𝖕 𝖒𝖊𝖓𝖚 !</b>

**𝒊𝒏 𝒕𝒉𝒊𝒔 𝒎𝒆𝒏𝒖 𝒚𝒐𝒖 𝒄𝒂𝒏 𝒐𝒑𝒆𝒏 𝒔𝒆𝒗𝒆𝒓𝒂𝒍 𝒂𝒗𝒂𝒊𝒍𝒂𝒃𝒍𝒆 𝒄𝒐𝒎𝒎𝒂𝒏𝒅 𝒎𝒆𝒏𝒖'𝒔, 𝒊𝒏 𝒆𝒂𝒄𝒉 𝒄𝒐𝒎𝒎𝒂𝒏𝒅 𝒎𝒆𝒏𝒖 𝒕𝒉𝒆𝒓𝒆 𝒊𝒔 𝒂𝒍𝒔𝒐 𝒂 𝒃𝒓𝒊𝒆𝒇 𝒆𝒙𝒑𝒍𝒂𝒏𝒂𝒕𝒊𝒐𝒏 𝒐𝒇 𝒆𝒂𝒄𝒉 𝒄𝒐𝒎𝒎𝒂𝒏𝒅**

⚡ __𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 {BOT_NAME} XmartySalim__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 ϐαѕιϲ ϲми∂", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 α∂ναиϲє∂ ϲми∂", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 α∂мιи ϲми∂", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 ѕυ∂ο ϲми∂", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 οωиєя ϲми∂", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 ƒυи ϲми∂", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🏓 `PONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
