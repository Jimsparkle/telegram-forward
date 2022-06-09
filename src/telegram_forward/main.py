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
COPY_CHAT = -1001763802535

app = Client(
    "TEST",
    phone_number=PHONE_NUM,
    api_id=API_ID,
    api_hash=API_HASH
)


@app.on_message(filters.chat(SOURCE_CHAT))
async def my_handler(client, message):
    # maybe the message is not initiated by user
    if not message.from_user:
        return
    elif "天天天" in message.from_user.first_name:
        await message.forward(COPY_CHAT)
    return


async def main():
    await app.start()
    await app.send_message(COPY_CHAT, "Ching Ba Monitor is now online!")

    await idle()

    await app.send_message(COPY_CHAT, "Ching Ba Monitor is now offline for maintanence!")
    await app.stop()


if __name__ == "__main__":
    app.run(main())
    