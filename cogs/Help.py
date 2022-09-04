import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self , client):
        self.client = client

    @commands.command(name="Help")

    async def help(self , ctx):
        
        embed = discord.Embed(title='Help:')
        embed.add_field(name='`!item [ITEM]`', value='Do this command to see an ingot.\nFor example: `!item amethyst_shard` to see the amethyst shard ingot.\n`--raw` can be used before the item name to see the raw image.', inline=False)
        embed.add_field(name='`!emoji [ITEM]`', value='Do this command to see an emoji.\nFor example: `!emoji flushed ingot` to see the flushed ingot emoji.', inline=False)
        await ctx.send(embed=embed)
      
async def setup(client):
    await client.add_cog(Help(client))
