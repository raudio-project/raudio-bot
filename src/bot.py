#!/usr/bin/env python3


import os

from discord.ext import commands
from dotenv import load_dotenv

from modules.Music import Music

# Load Token
load_dotenv()
TOKEN=os.getenv('BOT_TOKEN')
UID1=os.getenv('UID1')
UID2=os.getenv('UID2')
UID3=os.getenv('UID3')
UID4=os.getenv('UID4')

# Auth UIDs
AUTHENTICATED={int(UID1), int(UID2), int(UID3), int(UID4)}


bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description="Relatively simple music bot example",
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


bot.add_cog(Music(bot))
bot.run(TOKEN)
