import discord, requests
from discord.ext import commands

class Joke(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="joke")
    async def joke(self , ctx):
        
        r = requests.get('https://icanhazdadjoke.com', headers={"Accept": "text/plain"})
        await ctx.send(r.text)

async def setup(client):
    await client.add_cog(Joke(client))