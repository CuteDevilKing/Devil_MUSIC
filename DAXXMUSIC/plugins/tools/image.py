from ... import *
from pyrogram import *
from pyrogram.types import *

@app.on_message(filters.command("img"))
async def image(bot, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "Please Give Me a text to Generate Image ..."
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("Generating ...")
    text = message.text.split(None, 1)[1]
    resp = await api.imagine(text, 5)
    photo = resp["photos"]
    await message.reply_photo(photo=photo)
    await aux.delete()
