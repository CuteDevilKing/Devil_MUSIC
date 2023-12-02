from ... import *
from pyrogram import *
from pyrogram.types import *

@app.on_message(filters.command("coinfo"))
async def country(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "Please Give Me a Country Name to Get info..."
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("Processing ...")
    Country = message.text.split(None, 1)[1]
    try:
        resp = await api.ccgen(bin, 10)
        result = resp
        await aux.edit(result)
    except Exception as e:
        return await aux.edit(f"Error: {e}")
