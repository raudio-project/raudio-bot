from dataclasses import asdict

from discord.ext import commands

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def config(self, ctx):
        await ctx.send(f"Your current config is: {asdict(self.bot.config)}")

def setup(bot: commands.Bot):
    bot.add_cog(BasicCommands(bot))