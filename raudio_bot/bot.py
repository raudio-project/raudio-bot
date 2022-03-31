import os

from discord.ext import commands


class Raudio(commands.Bot):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = config

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    def reload_modules(self) -> None:
        for file in os.listdir("raudio/modules"):
            if file.endswith(".py"):
                print(f"Reloading {file[:-3]} module...")
                self.reload_extension(f"modules.{file[:-3]}")

    def load_modules(self) -> None:
        for file in os.listdir("raudio/modules"):
            if file.endswith(".py"):
                print(f"Loading {file[:-3]} module...")
                self.load_extension(f"modules.{file[:-3]}")

    def run(self, token):
        self.load_modules()
        super().run(token)
