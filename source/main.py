import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from libraryhelp import *
import embeds_messages

"""
    CONSTANTS
"""
load_dotenv('TOKEN.env')

GITHUB_CHANNEL = client.get_channel(963523231917146212)
LINKEDIN_CHANNEL = client.get_channel(963523353136738305)
WELCOME_CHANNEL = client.get_channel(963517870044749907)

BOT_PREFIX = '&'
"""
    CONSTANTS
"""


client = commands.Bot(command_prefix=BOT_PREFIX)
client.remove_command("help")

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await client.change_presence(activity=discord.Game("VS Code"))

"""
    Help => Display all commands
"""
@client.command()
async def help(ctx):
    help_message = help_embed()
    await ctx.send(embed = help_message)


"""
    Hello => Says hello to the user
"""
@client.command()
async def hello(ctx):
    author = ctx.author
    await ctx.send(f"Hello, {author.mention}!")

"""
    Info 
"""
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

"""
    Github =>
        add => Adds Github profile to accounts channel
        del => Deletes Github profile from accounts channel
"""
@client.command()
async def github(ctx, action = None, account = None):
    author = str(ctx.author.name)

    messages = await GITHUB_CHANNEl.history(limit=200).flatten()

    if action == None:
        await ctx.send(f"**Please add an action for command!**")
        return

    elif action == "add":
        for msg in messages:
            if author in str(msg.content):
                await msg.delete()
                await ctx.send("**You already have a github account.**")
                return
        
        await GITHUB_CHANNEL.send(f"[{author}](https://github.com/{account})")
        await ctx.send("**Github account successfully added!**")

    elif action == "del":
        for msg in messages:
            if author in str(msg.content):
                await ctx.send("**Github account successfully deleted!**")
                await msg.delete()
                return 

    else:
        await ctx.send("**Unknown command**")
        return

"""
    LinkedIn =>
        add => Adds LinkedIn profile to accounts channel
        del => Deletes LinkedIn profile from accounts channel
"""
@client.command()
async def linkedin(ctx, action = None, link = None):
    author = str(ctx.author.name)

    messages = await LINKEDIN_CHANNEL.history(limit=200).flatten()

    if action == None:
        await ctx.send(f"**Please add an action for command!**")
        return

    elif action == "add":
        for msg in messages:
            if author in str(msg.content):
                await msg.delete()
                await ctx.send("**You already have a LinkedIn account.**")
                return
        
        sent = await LINKEDIN_CHANNEL.send(f"[{author}]({link}")
        await ctx.send("**LinkedIn account successfully added!**")

    elif action == "del":
        for msg in messages:
            if author in str(msg.content):
                await ctx.send("**LinkedIn account successfully deleted!**")
                await msg.delete()
                return 
    
    else:
        await ctx.send("**Unknown command**")
        return


"""
    Welcome => test welcome
"""
@client.command()
async def welcome(ctx):
    member = ctx.author

    welcome_message = welcome_embed()
    
    await ctx.send(f"Welcome, {member.mention}", embed = welcome_message)

@client.event
async def on_member_join(member):
    welcome_message = welcome_embed()

    await WELCOME_CHANNEL.send(f"Welcome, {member.mention}", embed = welcome_message)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"**Invalid command**, use {BOT_PREFIX}help command for help.")


client.run(os.environ["TOKEN"])