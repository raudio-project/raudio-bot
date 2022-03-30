import os

from dataclasses import asdict
from unicodedata import name

from discord.ext import commands

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """ Test that Raudio is working """
        await ctx.send("Pong!")

    @commands.command()
    async def config(self, ctx):
        """ Print your current configuration settings"""
        await ctx.send(f"Your current config is: {asdict(self.bot.config)}")

    @commands.command()
    async def reload(self, ctx):
        """ Reload the current commands (for developers)"""
        self.bot.reload_modules()
        await ctx.send("Reloading commands...")

def setup(bot: commands.Bot):
    bot.add_cog(BasicCommands(bot))