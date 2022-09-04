import discord, os, asyncio, json

from http import client

from discord.ext import commands, tasks
from dotenv import load_dotenv

# get token
load_dotenv(os.path.join(os.path.dirname(__file__), 'configuration/.env'))

# get config
with open(os.path.join(os.path.dirname(__file__), 'configuration/config.json'), 'r') as config:
  get = json.load(config)

prefix = get['prefix']
  
# setup client
intents = discord.Intents().all()
client = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents, help_command=None)

@client.command()
async def load(ctx , extension):
  try:
    client.unload_extension(f"cogs.{extension}")
  except Exception:
    pass
  client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx , extension):
    client.unload_extension(f"cogs.{extension}")

@client.event
async def on_ready():
    print("ING-BØT online!")

# load cogs
async def load_extensions():
    for filename in os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/cogs'):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")

# login client
async def main():
    async with client:
        await load_extensions()
        await client.start(os.environ.get('TOKEN'))

asyncio.run(main())