
from pyrogram import Client
import asyncio
from VCPlayBot.config import SUDO_USERS
from VCPlayBot.config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from VCPlayBot.services.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Hɪ ᴛʜᴇʀᴇ, τнιѕ ιѕ α мυιѕϲ αѕѕιѕταиτ ѕєяνιϲє .\n\n ❗️ Rules:\n   - נοιи ѕυρροяτ gяουρ @xmarty_support\n   - иο ϲнαττιиg αℓℓοωє∂\n   - иο ѕραм αℓℓοωє∂ \n\n 👉 **ѕєи∂ gяουρ ιиνιτє ℓιиκ οя υѕєяиαмє ιƒ υѕєяϐοτ ϲαиϲτ γουя gяουρ.**\n\n ⚠️ ∂ιѕϲℓαмєя: ιƒ υя ѕєи∂ιиg α мαѕѕαgє нєяє ιτ мєαиѕ α∂мιи ωιℓℓ ѕєє γουя мєѕѕαgє αи∂ נοιи ϲнατ\n    - ∂οиϲτ α∂∂ τнιѕ υѕєя το ѕєϲєяτ gяουρѕ.\n   - ∂οиϲτ ѕнαяє υя ρяινατє ιиƒο нєяє\n\n",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("𝐏𝐦𝐩𝐞𝐫𝐦𝐢𝐭 𝐭𝐮𝐫𝐧𝐞𝐝 𝐨𝐧")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("𝐏𝐦𝐩𝐞𝐫𝐦𝐢𝐭 𝐭𝐮𝐫𝐧𝐞𝐝 𝐨𝐟𝐟")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("𝐀𝐩𝐩𝐫𝐨𝐨𝐯𝐞𝐝 𝐭𝐨 𝐏𝐌 𝐝𝐮𝐞 𝐭𝐨 𝐨𝐮𝐭𝐠𝐨𝐢𝐧𝐠 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("𝐀𝐩𝐩𝐫𝐨𝐨𝐯𝐞𝐝 𝐭𝐨 𝐏𝐌")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("𝐃𝐢𝐬𝐩𝐩𝐫𝐨𝐨𝐯𝐞𝐝 𝐭𝐨 𝐏𝐌")
        return
    message.continue_propagation()
