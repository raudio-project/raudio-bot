#!/usr/bin/env python3

import dataclasses
import os

from raudio_bot.bot import Raudio
from raudio_bot.config import raudio_config_from_json
from config import RaudioConfig

from discord.ext import commands
from dotenv import load_dotenv


import json

def check_for_file(file_name):
    if os.path.exists(file_name):
        return True
    else:
        x = input("Currently, there is no configuration specified for this bot. Would you like to create one? (y/n): ")

        if (x == 'y'):
            # get url and create data dictionary containing default specifications
            url = input("Enter URL of server you will be streaming from: ")

            # ADD ANY OTHER DEFAULT CONFIGS HERE
            data = RaudioConfig(stream_url=url, authenticated=[])
            
            datadict = dataclasses.asdict(data)

            # create default json file in upper directory
            with open('raudio_config.json','w') as jsonfile:
                json.dump(datadict, jsonfile)

            return True

        # if user does not then just return nothing
        else:
            return False



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

    if check_for_file("raudio_config.json"):    
        bot = Raudio(
            command_prefix=commands.when_mentioned_or("!"),
            description="Relatively simple music bot example",
            config=raudio_config_from_json("raudio_config.json"),
        )
        print(f"Using the following configuration: {dataclasses.asdict(bot.config)}")
        bot.run(token)


if __name__ == "__main__":
    main()

