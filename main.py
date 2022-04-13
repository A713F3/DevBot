import discord
import os
from dotenv import load_dotenv
from libraryhelp import *

load_dotenv('TOKEN.env')

client = discord.Client()

bot_command = '&'
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

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(bot_command):
        commands = str(message.content)[1:]
        parsed = commands.split(" ")

        command = low(parsed[0])
        arguments = list(map(low, parsed[1:]))

        if command not in bot_commands.keys():
            await message.channel.send(f"Invalid command, use {bot_command}help command for help.")
            return 

        print(f"\nAUTHOR: {message.author}")
        print(f"COMMAND: {command}")
        print(f"ARGUMENTS: {arguments}")
        
        if command == "help":
            await message.channel.send(f"> Command List:\n```{help_message}```")
            
        if command == "hello":
            author = str(message.author).split("#")
            await message.channel.send(f"Hello, {author[0]}")

        if command == "info":
            if len(arguments) < 2:
                await message.channel.send(f"Language and library argument needed!")
                return
            
            if arguments[0] == "-c":
                await message.channel.send(f"> **{arguments[1]}:** \n```{libraries_c[arguments[1]]}```")
            else:
                await message.channel.send(f"**Language not supported**,\nSupported languages => {language_list}")
            
            



client.run(os.environ["TOKEN"])