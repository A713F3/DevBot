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

GITHUB_ID = os.environ["GITHUB_ID"] 
LINKEDIN_ID = os.environ["LINKEDIN_ID"] 
WELCOME_ID = os.environ["WELCOME_ID"] 
ROLES_ID = os.environ["ROLES_ID"] 
TEST_ID = os.environ["TEST_ID"] 

REACTION_ID = ROLES_ID

PYTHON_REACTION = os.environ["PYTHON_REACTION"] 
C_REACTION = os.environ["C_REACTION"] 
JAVA_REACTION = os.environ["JAVA_REACTION"] 
KOTLIN_REACTION = os.environ["KOTLIN_REACTION"] 
JS_REACTION = os.environ["JS_REACTION"] 

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

SUCCESS_COLOR = 0x198754
FAIL_COLOR = 0xfc100d
BLACK_COLOR = 0x000006
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
    help_message = discord.Embed(title="How to use the DevBot :question:", description="- Useful Commands :rocket:-", color=BLACK_COLOR)
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
        fail = discord.Embed(title="Please add an action for command!", description=f"**Try:** {BOT_PREFIX}help", color=FAIL_COLOR)
        await ctx.send(embed=fail)
        return

    elif action == "add":
        if account == None:
            fail = discord.Embed(title="Please add an account!", description=f"**Try:** {BOT_PREFIX}help", color=FAIL_COLOR)
            await ctx.send(embed=fail)
            return

        for msg in messages:
            if author in str(msg.content):
                fail = discord.Embed(title="You already have a Github account.", description=f":mag_right: Github channel", color=FAIL_COLOR)
                await ctx.send(embed=fail)
                return

        await GITHUB_CHANNEL.send(f"[{ctx.author.mention}](https://github.com/{account})")

        success_add = discord.Embed(title="Github account successfully added!", description=":mag_right: Github channel", color=SUCCESS_COLOR)

        await ctx.send(embed=success_add)

    elif action == "del":
        for msg in messages:
            if author in str(msg.content):
                success_del = discord.Embed(title="Github account successfully deleted!", description=":mag_right: Github channel", color=SUCCESS_COLOR)
                await ctx.send(embed=success_del)
                await msg.delete()
                return

        fail_del = discord.Embed(title="You don't have a Github account!", description=":mag_right: Github channel", color=FAIL_COLOR)
        await ctx.send(embed=fail_del)

    else:
        fail = discord.Embed(title="Unknown command", description=f"**Try:** {BOT_PREFIX}help", color=FAIL_COLOR)
        await ctx.send(embed=fail)
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
        fail = discord.Embed(title="Please add an action for command!", description=f"**Try:** {BOT_PREFIX}help", color=FAIL_COLOR)
        await ctx.send(embed=fail)
        return

    elif action == "add":
        if link == None:
            fail = discord.Embed(title="Please add an account!", description=f"**Try:** {BOT_PREFIX}help", color=FAIL_COLOR)
            await ctx.send(embed=fail)
            return

        for msg in messages:
            if author in str(msg.content):
                fail = discord.Embed(title="You already have a LinkedIn account.", description=f":mag_right: LinkedIn channel", color=FAIL_COLOR)
                await ctx.send(embed=fail)
                return

        await LINKEDIN_CHANNEL.send(f"[{ctx.author.mention}]({link})")

        success_add = discord.Embed(title="LinkedIn account successfully added!", description=":mag_right: LinkedIn channel", color=SUCCESS_COLOR)

        await ctx.send(embed=success_add)

    elif action == "del":
        for msg in messages:
            if author in str(msg.content):
                success_del = discord.Embed(title="LinkedIn account successfully deleted!", description=":mag_right: LinkedIn channel", color=SUCCESS_COLOR)
                await ctx.send(embed=success_del)
                await msg.delete()
                return

        fail_del = discord.Embed(title="You don't have a LinkedIn account!", description=":mag_right: LinkedIn channel", color=FAIL_COLOR)
        await ctx.send(embed=fail_del)

    else:
        fail = discord.Embed(title="Unknown command", description=f"**Try:** {BOT_PREFIX}help", color=FAIL_COLOR)
        await ctx.send(embed=fail)
        return


"""
    Admin commands
"""
@client.command()
@commands.has_role("Admin")
async def role(ctx):
    ROLES_CHANNEL = client.get_channel(REACTION_ID)

    labels = f"{PYTHON_REACTION}-Python {C_REACTION}-C/C++ {JAVA_REACTION}-Java {JS_REACTION}-JavaScript {KOTLIN_REACTION}-Kotlin"

    role_embed = discord.Embed(title="Please choose your roles:", description=":mag_right: **Hint:** React to this message.", color=BLACK_COLOR)
    role_embed.add_field(name=labels, value="(Multiple choice is available)")
    role_embed.set_image(url=DEVBOT_IMAGE)

    message = await ROLES_CHANNEL.send(embed=role_embed)

    for reaction in REACTIONS.keys():
        await message.add_reaction(reaction)


@client.command()
@commands.has_role("Admin")
async def rules(ctx):
    ROLES_CHANNEL = client.get_channel(REACTION_ID)

    rules = discord.Embed(title=":page_facing_up: Rules:", description="General rules of this server.")
    rules.add_field(name=":handshake: Supportive", value="Be encouraging in your comments. Evaluate the words spoken and the work done in a positive way.")
    rules.add_field(name=":slight_smile: Respectful", value="Respect every individual. Do not use language or act in a way that hurts or insults anyone. Insults, sexism, racism or hate speech will not be tolerated.")
    rules.add_field(name=":man_detective: Spam-Free", value="Do not send too many small messages one after the other. Do not interrupt the conversation by sending spam.")
    rules.add_field(name=":bust_in_silhouette: Follow the Discord Community Guidelines", value="You can find it here: https://discord.com/guidelines")

    await ROLES_CHANNEL.send(embed=rules)

@client.command()
@commands.has_role("Admin")
async def clear(ctx, limit=200):
    await ctx.channel.purge(limit=limit)

@client.command()
@commands.has_role("Admin")
async def welcome(ctx):
    member = ctx.author

    welcome_message = discord.Embed(title=":coffee: Grab a cup of coffee and start coding...", description=":mag_right: **Hint:** try &help", color=BLACK_COLOR)
    await ctx.send(f"Welcome, {member.mention}", embed = welcome_message)

"""
    Admin commands
"""

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

    welcome_message = discord.Embed(title=":coffee: Grab a cup of coffee and start coding...", description=":mag_right: **Hint:** try &help", color=BLACK_COLOR)

    await WELCOME_CHANNEL.send(f"Welcome, {member.mention}", embed = welcome_message)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        error = discord.Embed(title="Invalid command", description=f"**Try:** {BOT_PREFIX}help", color=FAIL_COLOR)
        await ctx.send(embed=error)


client.run(os.environ["TOKEN"])
