import discord
from discord.ext import commands

class Template(commands.Cog):

    def __init__(self , client):
        self.client = client

    @commands.command(name="")
    async def template(self , ctx):        
      await ctx.send('Hello World!')

      
async def setup(client):
    await client.add_cog(Template(client))