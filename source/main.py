import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from libraryhelp import *

"""
    CONSTANTS
"""
load_dotenv('TOKEN.env')

BOT_PREFIX = '&'
intents = discord.Intents.all()
client = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

GITHUB_ID = 963523231917146212
LINKEDIN_ID = 963523353136738305
WELCOME_ID = 963517870044749907
ROLES_ID = 965952759918632980
TEST_ID = 963536301762678797

REACTION_ID = ROLES_ID

PYTHON_REACTION = "🐍"
C_REACTION = "🇨"

PYTHON_ROLE_NAME = "python"
C_ROLE_NAME = "C"
"""
    CONSTANTS
"""
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
    help_message = discord.Embed(title="How to use the DevBot :question:", description="- Useful Commands :rocket:-", color=0x000006)
    help_message.add_field(name="&help", value="- Display all commands")
    help_message.add_field(name="&hello", value="- Says hello to the user")
    help_message.add_field(name="&github add (username)", value="- Adds Github profile to accounts channel")
    help_message.add_field(name="&github del", value="- Deletes Github profile from accounts channel")
    help_message.add_field(name="&linkedin add (account link)", value="- Adds LinkedIn profile to accounts channel")
    help_message.add_field(name="&linkedin del", value="- Deletes LinkedIn profile from accounts channel")
    help_message.set_image(url="https://github.com/A713F3/DevBot/blob/master/devbot.png?raw=true")

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

    GITHUB_CHANNEL = client.get_channel(GITHUB_ID)

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

    LINKED_CHANNEL = client.get_channel(LINKEDIN_ID)

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

@client.command()
async def role(ctx):
    ROLES_CHANNEL = client.get_channel(REACTION_ID)

    role_embed = discord.Embed(title="To enter the server please state your roles:", description=":mag_right: **Hint:** React to this message.", color=0x000006)
    role_embed.add_field(name=":snake: - Python  :regional_indicator_c: - C", value="(Multiple choice is available)")
    role_embed.set_image(url="https://github.com/A713F3/DevBot/blob/master/devbot.png?raw=true")

    message = await ROLES_CHANNEL.send(embed=role_embed)

    await message.add_reaction(PYTHON_REACTION)
    await message.add_reaction(C_REACTION)


"""
    Welcome => test welcome
"""
@client.command()
async def welcome(ctx):
    member = ctx.author

    welcome_message = discord.Embed(title=":coffee: Grab a cup of coffee and start coding...", description=":mag_right: **Hint:** try &help", color=0x000006)    
    await ctx.send(f"Welcome, {member.mention}", embed = welcome_message)


@client.event
async def on_reaction_add(reaction, user):
    print("add girdi")
    if reaction.message.channel.id != REACTION_ID:
        return
    
    if reaction.emoji == PYTHON_REACTION:
        python_role = discord.utils.get(user.guild.roles, name=PYTHON_ROLE_NAME)
        await user.add_roles(python_role)


    if reaction.emoji == C_REACTION:
        c_role = discord.utils.get(user.guild.roles, name=C_ROLE_NAME)
        await user.add_roles(c_role)


@client.event
async def on_reaction_remove(reaction, user):
    print("remove girdi")
    if reaction.message.channel.id != REACTION_ID:
        return

    if reaction.emoji == PYTHON_REACTION:
        python_role = discord.utils.get(user.guild.roles, name=PYTHON_ROLE_NAME)
        try:
            await user.remove_roles(python_role)
        except:
            pass

    if reaction.emoji == C_REACTION:
        c_role = discord.utils.get(user.guild.roles, name=C_ROLE_NAME)
        try:
            await user.remove_roles(c_role)
        except:
            pass


@client.event
async def on_member_join(member):
    WELCOME_CHANNEL = client.get_channel(WELCOME_ID)

    welcome_message = discord.Embed(title=":coffee: Grab a cup of coffee and start coding...", description=":mag_right: **Hint:** try &help", color=0x000006)

    await WELCOME_CHANNEL.send(f"Welcome, {member.mention}", embed = welcome_message)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"**Invalid command**, use {BOT_PREFIX}help command for help.")


client.run(os.environ["TOKEN"])