import discord, asyncio, random
from discord.ext import commands
from PIL import Image

class Make(commands.Cog):

    def __init__(self , client):
        self.client = client

    @commands.command(name="make")
    async def make(self, ctx: commands.Context, *, args: str = None):
        if args == None:
            await ctx.send("You can't make nothing into something.")
            return
        
        args = args.split(" ")

        embed = discord.Embed(title='Here is your Ingot OC:tm:')

        colour = (int(args[0][:2], base=16), int(args[0][-4:4], base=16), int(args[0][-2:], base=16))

        if len(args) < 2:
            args[1] = "iron"

        empty = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
        base = Image.new("RGBA", (16, 16), colour)

        try:
            texture = Image.open('assets/patterns/{}.png'.format(args[1]))
        except:
            embed = discord.Embed(title="{} does not exist as a pattern.".format(args[1]))
            embed.colour = 0xFF0000
            if random.randint(0, 999) == 0:
                embed.set_footer(text="Skill issue")
            else:
                embed.set_footer(text="This message will will self destruct in 10 seconds...")
            m = await ctx.send(embed=embed)
            await asyncio.sleep(10)
            await m.delete()
            return

        mask = Image.open('assets/mask.png')
        base.paste(texture, (0, 0), texture)
        base = Image.composite(empty, base, mask)
        base = base.resize((base.width * 10, base.height * 10), Image.NEAREST)

        base.save("assets/temp.png")

        file = discord.File("assets/temp.png", filename="ingot.png")
        embed.set_image(url="attachment://ingot.png")

        await ctx.send(embed=embed, file=file)

      
async def setup(client):
    await client.add_cog(Make(client))