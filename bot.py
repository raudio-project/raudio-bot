#!/usr/bin/python3

import asyncio

import youtube_dl
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

# Load Token
load_dotenv()
TOKEN=os.getenv('BOT_TOKEN')
UID1=os.getenv('UID1')
UID2=os.getenv('UID2')
UID3=os.getenv('UID3')
UID4=os.getenv('UID4')

# Auth UIDs
AUTHENTICATED={int(UID1), int(UID2), int(UID3), int(UID4)}

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ""


ytdl_format_options = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",  # Bind to ipv4 since ipv6 addresses cause issues at certain times
}

ffmpeg_options = {"options": "-vn"}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(
            None, lambda: ytdl.extract_info(url, download=not stream)
        )

        if "entries" in data:
            # Takes the first item from a playlist
            data = data["entries"][0]

        filename = data["url"] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx):
        """Resumes playing of stream"""

        if ctx.message.author.id in AUTHENTICATED:
            # TODO PUT request to /play
            await ctx.send("Resuming stream")
        else:
            # DO nothing (non auth user)
            await ctx.send("You are not able to do that")

    @commands.command()
    async def pause(self, ctx):
        """Pauses stream"""

        if ctx.message.author.id in AUTHENTICATED:
            # TODO PUT request to /pause
            await ctx.send("Pausing stream")
        else:
            # DO nothing (non auth user)
            await ctx.send("You are not able to do that")

    @commands.command()
    async def skip(self, ctx):
        """Resumes playing of stream"""

        if ctx.message.author.id in AUTHENTICATED:
            # TODO PUT request to /skip
            await ctx.send("Playing next song")
        else:
            # DO nothing (non auth user)
            await ctx.send("You are not able to do that")

    @commands.command()
    async def listen(self, ctx):
        """Streams from server"""
        url = "http://momo.campus.nd.edu:5000/stream"
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(
                player, after=lambda e: print(f"Player error: {e}") if e else None
            )

        await ctx.send(f"Now playing Raudio Mix")

    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @listen.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


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
