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
TEST_ID = 966369041310699642

REACTION_ID = ROLES_ID

PYTHON_REACTION = "<:phy:965995904391864391>"
C_REACTION = "<:c_:965996476654301214>"
JAVA_REACTION = "<:jav:965998639036121091>"
KOTLIN_REACTION = "<:kot:965997900071047228>"
JS_REACTION = "<:js:965996881933127759>"

PYTHON_ROLE_NAME = "Python"
C_ROLE_NAME = "C"
JAVA_ROLE_NAME = "Java"
KOTLIN_ROLE_NAME = "Kotlin"
JS_ROLE_NAME = "JavaScript"

REACTIONS ={PYTHON_REACTION : PYTHON_ROLE_NAME, 
            C_REACTION      : C_ROLE_NAME, 
            JAVA_REACTION   : JAVA_ROLE_NAME,
            KOTLIN_REACTION : KOTLIN_ROLE_NAME,
            JS_REACTION     : JS_ROLE_NAME
            }

DEVBOT_IMAGE = "https://raw.githubusercontent.com/A713F3/DevBot/master/images/devbot_img.png"
DEVBOT_HELP_IMAGE = "https://raw.githubusercontent.com/A713F3/DevBot/master/images/devbot_help_img.png"

GITHUB_PP_API = "https://avatars.githubusercontent.com/"
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
    help_message.set_thumbnail(url=DEVBOT_HELP_IMAGE)

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
    author = str(ctx.author.id)

    GITHUB_CHANNEL = client.get_channel(GITHUB_ID)

    messages = await GITHUB_CHANNEL.history(limit=200).flatten()
    
    if action == None:
        await ctx.send(f"**Please add an action for command!**")
        return

    elif action == "add":
        if account == None:
            await ctx.send(f"**Please add an account!**")
            return 

        for msg in messages:
            if author in str(msg.content):
                await ctx.send("**You already have a github account.**")
                return
        
        await GITHUB_CHANNEL.send(f"[{ctx.author.mention}](https://github.com/{account})")
        await ctx.send("**Github account successfully added!**")

    elif action == "del":
        for msg in messages:
            if author in str(msg.content):
                await ctx.send("**Github account successfully deleted!**")
                await msg.delete()
                return 
        await ctx.send("**You don't have a Github account!**")

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
    author = str(ctx.author.id)

    LINKEDIN_CHANNEL = client.get_channel(LINKEDIN_ID)

    messages = await LINKEDIN_CHANNEL.history(limit=200).flatten()

    if action == None:
        await ctx.send(f"**Please add an action for command!**")
        return

    elif action == "add":
        if link == None:
            await ctx.send(f"**Please add an account!**")
            return 

        for msg in messages:
            if author in str(msg.content):
                await ctx.send("**You already have a LinkedIn account.**")
                return
        
        sent = await LINKEDIN_CHANNEL.send(f"[{ctx.author.mention}]({link}")
        await ctx.send("**LinkedIn account successfully added!**")

    elif action == "del":
        for msg in messages:
            if author in str(msg.content):
                await ctx.send("**LinkedIn account successfully deleted!**")
                await msg.delete()
                return 
        await ctx.send("**You don't have a LinkedIn account!**")
    
    else:
        await ctx.send("**Unknown command**")
        return

@client.command()
async def role(ctx):
    ROLES_CHANNEL = client.get_channel(REACTION_ID)

    labels = f"{PYTHON_REACTION}-Python {C_REACTION}-C/C++ {JAVA_REACTION}-Java {JS_REACTION}-JavaScript {KOTLIN_REACTION}-Kotlin"

    role_embed = discord.Embed(title="To enter the server please state your roles:", description=":mag_right: **Hint:** React to this message.", color=0x000006)
    role_embed.add_field(name=labels, value="(Multiple choice is available)")
    role_embed.set_image(url=DEVBOT_IMAGE)

    message = await ROLES_CHANNEL.send(embed=role_embed)

    for reaction in REACTIONS.keys():
        await message.add_reaction(reaction)


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
    if reaction.message.channel.id != REACTION_ID:
        return

    if str(reaction.emoji) in REACTIONS.keys():
        role_name = REACTIONS[str(reaction.emoji)]

        role = discord.utils.get(user.guild.roles, name=role_name)

        await user.add_roles(role)


@client.event
async def on_reaction_remove(reaction, user):
    if reaction.message.channel.id != REACTION_ID:
        return

    if str(reaction.emoji) in REACTIONS.keys():
        role_name = REACTIONS[str(reaction.emoji)]

        role = discord.utils.get(user.guild.roles, name=role_name)

        await user.remove_roles(role)


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