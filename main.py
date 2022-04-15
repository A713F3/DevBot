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

github_profiles = {}
linkedin_profiles = {}




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
async def github(ctx, action = None, account = None):
    author = str(ctx.author).split("#")
    # 963523231917146212 // main server id
    github_channel = client.get_channel(963523231917146212)

    messages = await github_channel.history(limit=200).flatten()

    if action == None:
        await ctx.send(f"**Please add an action for command!**")
        return

    elif action == "add":
        for msg in messages:
            if author[0] in str(msg.content):
                await msg.delete()
                await ctx.send("**You already have a github account.**")
                return
        
        sent = await github_channel.send(f"[{author[0]}](https://github.com/{account})")
        await ctx.send("**Github account successfully added!**")

    elif action == "del":
        for msg in messages:
            if author[0] in str(msg.content):
                await ctx.send("**Github account successfully deleted!**")
                await msg.delete()
                return 

    else:
        await ctx.send("**Unknown command**")
        return

@client.command()
async def linkedin(ctx, action = None, link = None):
    author = str(ctx.author).split("#")
    # 963523353136738305 // main server id
    linkedin_channel = client.get_channel(963523353136738305)

    messages = await linkedin_channel.history(limit=200).flatten()

    if action == None:
        await ctx.send(f"**Please add an action for command!**")
        return

    elif action == "add":
        for msg in messages:
            if author[0] in str(msg.content):
                await msg.delete()
                await ctx.send("**You already have a LinkedIn account.**")
                return
        
        sent = await linkedin_channel.send(f"[{author[0]}]({link}")
        await ctx.send("**LinkedIn account successfully added!**")

    elif action == "del":
        for msg in messages:
            if author[0] in str(msg.content):
                await ctx.send("**LinkedIn account successfully deleted!**")
                await msg.delete()
                return 
    
    else:
        await ctx.send("**Unknown command**")
        return

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"**Invalid command**, use {bot_prefix}help command for help.")


client.run(os.environ["TOKEN"])