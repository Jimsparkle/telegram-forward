from pyrogram import Client, filters, idle
from pyrogram.handlers import MessageHandler

from decouple import config

import logging


LOGGER = logging.getLogger(__name__)

# exposed by .env
API_ID = config('API_ID')
API_HASH = config('API_HASH')
PHONE_NUM = config('PHONE_NUM')

# CHAT ID
SOURCE_CHAT = -1001244925080
SOURCE_CHANNEL = -1001446754046
COPY_CHAT = -1001763802535

app = Client(
    "TEST",
    phone_number=PHONE_NUM,
    api_id=API_ID,
    api_hash=API_HASH
)


# FROM THE GROUP CHAT
@app.on_message(filters.chat(SOURCE_CHAT))
async def my_handler(client, message):
    # maybe the message is not initiated by user
    if not message.from_user:
        return
    elif "天天天" in message.from_user.first_name:  # 
        # is he replying any message?
        original_message = message.reply_to_message
        if original_message:
            await original_message.forward(COPY_CHAT)
            await app.send_message(COPY_CHAT, "↑↑↑↑↑↑ MEMBER COPIED ↑↑↑↑↑↑ | ↓↓↓↓↓ CHING BA REPLY ↓↓↓↓↓")
            await message.forward(COPY_CHAT)
        else:
            await message.forward(COPY_CHAT)
    return


# FROM HIS CHANNEL
@app.on_message(filters.chat(SOURCE_CHANNEL))
async def my_handler(client, message):
    await message.forward(COPY_CHAT)
    return


async def main():
    await app.start()

    await idle()

    await app.stop()


if __name__ == "__main__":
    app.run(main())
    