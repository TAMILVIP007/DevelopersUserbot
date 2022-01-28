from pyrogram.types import *
from _pyrogram import *
from pyrogram import *
from config import *
from os import *

@app.on_message(filters.command("json", PREFIX) & filters.me)
async def start(client, message):
    try:
        msg = message.reply_to_message or message
        if len(str(msg_info)) > int("4096"):
            with open("json.txt", "w+") as file:
                file.write(str(msg_info))
            await app.send_document(
                message.chat.id,
                "json.txt",
                caption="Returned JSon",

            )
            remove("json.txt")

        else:
            await message.edit(str(msg_info))

    except Exception as e:
        await message.edit(f"{e}")
