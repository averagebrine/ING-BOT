import asyncio
from re import I
import discord, os, json, requests, random
from discord.ext import commands
from github import Github
from dotenv import load_dotenv
from time import sleep


class Desc(commands.Cog):

    def __init__(self , client):
        self.client = client

    @commands.command(name="desc")
    async def desc(self, ctx: commands.Context, *, args: str = None):

        # skill issue function
        async def error_embed(args: str = None):
            embed = discord.Embed(title=args)
            embed.colour = 0xFF0000

            if random.randint(0, 7) == 0:
                embed.set_footer(text="Skill issue")
            else:
                embed.set_footer(text="This message will will self destruct in 10 seconds...")

            m = await ctx.send(embed=embed)
            await asyncio.sleep(10)
            await m.delete()

        # authentication and authorization
        trusted = json.load(open("configuration/coolppl.json"))

        if not ctx.author.id in trusted:
            await error_embed("You are not authorized to use this command, young cultist!")
            return

        # if we don't have any args, we can't do anything. silly boy
        if args == None:
            await error_embed("There is no description...")
            return

        # format the imput into 2 arguments
        try:
            args = args.split("=")
            args[0] = args[0].lower().rstrip(' ').replace(" ", "_")
            args[1] = args[1].lstrip(' ')
        except:
            await error_embed("Incorrect arguments! (Usage: iron ingot  = ingot description)")
            return

        if len(args) != 2:
            await error_embed("Incorrect arguments! (Usage: iron ingot  = ingot description)")
            return

        # do stuff time!!!
        load_dotenv("configuration/.env")
        os.environ.get('GITHUB_TOKEN')

        g = Github(os.environ.get("GITHUB_TOKEN"))

        # if the item doesn't exist, we can't write a description for it. silly boy
        item = requests.get("https://raw.githubusercontent.com/WaspVentMan/Ingot-Pack/main/assets/minecraft/textures/item/" + args[0] + ".png")
        if not item:
            await error_embed("That item doesn't exist! Yet...")
            return

        # the holy repo
        repo = g.get_repo("WaspVentMan/Ingot-Pack")

        # this is lazy but it works just fine
        desc = requests.get("https://raw.githubusercontent.com/WaspVentMan/Ingot-Pack/main/assets/ingot_cult/ing-bot/desc/" + args[0] + ".txt")
        if desc:
            contents = repo.get_contents("assets/ingot_cult/ing-bot/desc/" + args[0] + ".txt")
            repo.delete_file(contents.path, "Automated commit by ING-BØT!", contents.sha, branch="main")


        if args[1] != "":
            repo.create_file("assets/ingot_cult/ing-bot/desc/" + args[0] + ".txt", "Automated commit by ING-BØT!", args[1], branch="main")

        # great success
        embed = discord.Embed(title="Great success!", color=0x3ba55d)

        if args[1] != "":
            embed.description = "The description has been implemented!"
        else:
            embed.description = "The description has been removed!"

        if random.randint(0, 8) == 0:
            embed.set_footer(text="Skill issue")
        else:
            embed.set_footer(text="This message will will self destruct in 10 seconds...")
        
        m = await ctx.send(embed=embed)
        await asyncio.sleep(10)
        await m.delete()

async def setup(client):
    await client.add_cog(Desc(client))