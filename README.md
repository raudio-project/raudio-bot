# raudio-bot
This project is a Discord bot written in Python as a client for the Raudio 
server. At the moment, it just a proof of concept in order to be an example
for one of many clients you could build Raudio.

## Installation

Install the package, optionally in a virtual environment:

`pip install raudio-bot`

Create the appropriate configuration files. See **Setting your token** and
**Creating a bot configuration** below.

Finally, run the bot:

`python3 -m raudio_bot`

## Setting up a development environment
In order to develop for the Raudio bot, first you must obtain a token from
Discord for authenticating your bot. You can do this by visiting the [Discord
Developer Portal](https://discord.com/developers/applications) and creating an
application. From there you can generate a token for the bot.


### Downloading the project
Clone the repository with the following:

```sh
$ git clone git@github.com:raudio-project/raudio-bot.git
$ cd raudio-bot
$ python3 -m venv venv             # Create a python virtual environment
$ source venv/bin/activate         # Activate the dev environment
$ pip3 install                     # Install dependencies for the project
```

### Setting your token
Now, specify the token by creating a `.env` file inside of the `raudio-bot`
folder. 

```sh
echo "BOT_TOKEN=your_token_goes_here" >> .env
```

### Creating a bot configuration
Third, you must create a configuration for the bot. Create a `raudio_config.json`
with the following:

```json
{
    "stream_url": "http://momo.campus.nd.edu:5000/stream",
    "authenticated": [
        
    ]
}
```

Currently, the `stream_url` field corresponds to the URL where the raudio
server is set to. You may, of course, host your own, but feel free to use
the hosted version. This URL is only available to University of Notre Dame
students signed into the `eduroam` network, due to the university firewall.

### Running the bot
Now you should be all set up! Simply run the following

```
$ python3 raudio
```

## License
GPL-3.0
