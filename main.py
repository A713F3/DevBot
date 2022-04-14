import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from libraryhelp import *

load_dotenv('TOKEN.env')

bot_prefix = '&'
client = commands.Bot(command_prefix=bot_prefix)
client.remove_command("help")

bot_commands = {
    "help":" => Show commands.", 
    "hello":" => Greets user", 
    "info":" -language -library => Shows information about library."
    }
help_message = "\n".join([c + bot_commands[c] for c in bot_commands.keys()])




def low(str):
    return str.lower()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Game("VS Code"))

@client.command()
async def help(ctx):
    await ctx.send(f"```{help_message}```")

@client.command()
async def hello(ctx):
    author = str(ctx.author).split("#")
    await ctx.send(f"Hello, {author[0]}")

@client.command()
async def info(ctx, language = None, library = None):
    if language == None or library == None:
        await ctx.send(f"**Language and library argument needed!**")
        return

    language = language.lower()
    library = library.lower()

    if language == "-c":
        await ctx.send(f"> **{library}:** \n```{libraries_c[library]}```")
    else:
        await ctx.send(f"**Language not supported**,\nSupported languages => {language_list}")

@client.command()
async def github(ctx, account):
    author = str(ctx.author).split("#")
    github_channel = client.get_channel(963523231917146212)

    await github_channel.send(f"[{author[0]}](https://github.com/{account})")

@client.command()
async def linkedin(ctx, link):
    author = str(ctx.author).split("#")
    github_channel = client.get_channel(963523353136738305)
    
    await github_channel.send(f"[{author[0]}]({link})")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"**Invalid command**, use {bot_prefix}help command for help.")


client.run(os.environ["TOKEN"])