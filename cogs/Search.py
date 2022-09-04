import discord, os, asyncio, random, requests, urllib.request
from discord.ext import commands
from PIL import Image

class Search(commands.Cog):

    def __init__(self , client):
        self.client = client

    @commands.command(name="item")
    async def item(self, ctx: commands.Context, *, args: str = None):
        try:
            if args == None:
                embed = discord.Embed(title="Nothing isn't an item yet, sorry.")
                embed.colour = 0xFF0000
                embed.set_footer(text="This message will will self destruct in 10 seconds...")
                m = await ctx.send(embed=embed)
                await asyncio.sleep(10)
                await m.delete()
                return

            if args.startswith("--raw "):
                raw = True
                args = args.replace("--raw ", "")
            else: raw = False
            args = args.lower().replace(" ", "_")
            
            #Ingo descripto
            desc = requests.get('https://raw.githubusercontent.com/WaspVentMan/Ingot-Pack/main/assets/ingot_cult/sip/desc/' + args + '.txt').content.decode('utf-8')
            if desc != '404: Not Found':
                embed = discord.Embed(title=args.replace("_", " ").title(), description=desc, url='https://github.com/WaspVentMan/Ingot-Pack/blob/main/assets/minecraft/textures/item/' + args + '.png')
            else:
                embed = discord.Embed(title=args.replace("_", " ").title(), url='https://github.com/WaspVentMan/Ingot-Pack/blob/main/assets/minecraft/textures/item/' + args + '.png')
            
            embed.set_footer(text="Texture unfinished?\nComplete it yourself and add it to the GitHub!")

            #dumb rendering time!!!!
            url = "https://raw.githubusercontent.com/WaspVentMan/Ingot-Pack/main/assets/minecraft/textures/item/" + args + ".png"
            
            urllib.request.urlretrieve(url, "temp/temp.png")

            if not raw:
                base = Image.open('assets/backing.png')
                ingot = Image.open('temp/temp.png').convert("RGBA")

                ex = []
                for x in range(8):
                    ex.append(Image.open('assets/ingots/{}'.format(os.listdir("assets/ingots")[random.randint(0, len(os.listdir("assets/ingots"))-1)])).convert("RGBA"))

                base.paste(ingot, (6, 6),     ingot)
                base.paste(ex[0], (-12, 6),   ex[0])
                base.paste(ex[1], (24, 6),    ex[1])
                base.paste(ex[2], (6, -12),   ex[2])
                base.paste(ex[3], (6, 24),    ex[3])
                base.paste(ex[4], (-12, -12), ex[4])
                base.paste(ex[5], (24, -12),  ex[5])
                base.paste(ex[6], (-12, 24),  ex[6])
                base.paste(ex[7], (24, 24),   ex[7])

                base = base.resize((base.width * 10, base.height * 10), Image.NEAREST)

                base.save("temp/temp.png")

            file = discord.File("temp/temp.png", filename="ingot.png")
            embed.set_image(url="attachment://ingot.png")

            await ctx.send(embed=embed, file=file)

        # Error handling lmao
        except Exception as e:
            embed = discord.Embed(title=e)
            embed.colour = 0xFF0000
            if random.randint(0, 4) == 0:
                embed.set_footer(text="Skill issue")
            else:
                embed.set_footer(text="This message will will self destruct in 10 seconds...")
            m = await ctx.send(embed=embed)
            await asyncio.sleep(10)
            await m.delete()
    
    @commands.command(name="emoji")
    async def emoji(self, ctx: commands.Context, *, args: str = None):
        try:
            if args == None:
                await ctx.send("You need to enter an item name, nothing isn't an item.")
                return

            args = args.lower().replace(" ", "_")

            #Ingo descripto
            desc = requests.get('https://raw.githubusercontent.com/WaspVentMan/Ingot-Pack/main/assets/ingot_cult/sip/desc/' + args + '.txt').content.decode('utf-8')
            if desc != '404: Not Found':
                embed = discord.Embed(title=args.replace("_", " ").title(), description=desc, url='https://github.com/WaspVentMan/Ingot-Pack/blob/main/assets/minecraft/textures/item/' + args + '.png')

            else:
                embed = discord.Embed(title=args.replace("_", " ").title(), url='https://github.com/WaspVentMan/Ingot-Pack/blob/main/assets/minecraft/textures/item/' + args + '.png')
            
            #dumb rendering time!!!!
            url = "https://raw.githubusercontent.com/WaspVentMan/Ingot-Pack/main/assets/ingot_cult/emoji/" + args + ".png"
            
            urllib.request.urlretrieve(url, "temp/temp.png")

            file = discord.File("temp/temp.png", filename="ingot.png")
            embed.set_image(url="attachment://ingot.png")

            await ctx.send(embed=embed, file=file)

        # Error handling lmao
        except Exception as e:
            embed = discord.Embed(title=e)
            embed.colour = 0xFF0000
            if random.randint(0, 999) == 0:
                embed.set_footer(text="Skill issue")
            else:
                embed.set_footer(text="This message will will self destruct in 10 seconds...")
            m = await ctx.send(embed=embed)
            await asyncio.sleep(10)
            await m.delete()
      
async def setup(client):
    await client.add_cog(Search(client))