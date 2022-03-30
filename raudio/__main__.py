#!/usr/bin/env python3

import os

from bot import Raudio
from config import raudio_config_from_json

from discord.ext import commands
from dotenv import load_dotenv


def load_token() -> str:
    load_dotenv()

    if not (token := os.getenv("BOT_TOKEN")):
        raise Exception(
            "Token cannot be loaded. Do you have a .env with a BOT_TOKEN field?"
        )

    return token


def main() -> None:
    """Parse command line arguments and pass configuration to bot"""
    token = load_token()

    bot = Raudio(
        command_prefix=commands.when_mentioned_or("!"),
        description="Relatively simple music bot example",
        config=raudio_config_from_json("raudio_config.json"),
    )

    bot.run(token)


if __name__ == "__main__":
    main()
