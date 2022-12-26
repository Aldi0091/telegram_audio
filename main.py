from telethon import TelegramClient, events, connection
from conf import api_hash, api_id, bot_token
from telethon.tl.functions.messages import GetDialogsRequest
import asyncio


API_HASH = api_hash
API_ID = api_id
BOT_TOKEN = bot_token
USER_NAME = "fav_stack_bot"


client = TelegramClient("data_thief", API_ID, API_HASH)

async def main():
    
    users = []

    async for dialog in client.iter_dialogs():
        users.append(dialog.entity.username)

    for user in users:
        if user == "ddvp2":
            async for mess in client.iter_messages(user):
                print(mess.sender_id, ":", mess.text)
        if user is not None:
            await client.download_profile_photo(user)

with client:
    client.loop.run_until_complete(main())

# async def main():
#     # Now you can use all client methods listed below, like for example...
#     await client.send_message('me', 'Hello to myself!')

# with client:
#     client.loop.run_until_complete(main())
# client = TelegramClient('data_thief', API_ID, API_HASH)

# client.connect()
# client.start()
# bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# @bot.on(events.NewMessage(pattern='^/open$'))
# async def open(event):
#     print("running")
#     
#     await event.respond("opened")

# with TelegramClient("data_thief", API_ID, API_HASH) as client: 
#     result = client(GetDialogsRequest(
#             offset_date = None,
#             offset_id = 0,
#             offset_peer = "username",
#             limit = 500,
#             hash = 0,
#         ))
#     for res in result.users:
#         print(res)