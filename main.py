from os import environ
from pyrogram import Client, idle

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
session_string = environ["SESSION_NAME"]

plugins = dict(
    root="plugins",
    include=[
        "vc." + environ["PLUGIN"],
        "ping",
        "sysinfo"
    ]
)

app = Client(
    "vcfighter",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session_string,
    plugins=plugins
)

app.start()
print(">>> USERBOT STARTED by @YogeshBots")

idle()

app.stop()
print("\n>>> USERBOT STOPPED by @YogeshBots")
