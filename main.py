import discord
import os
from dotenv import load_dotenv

load_dotenv('TOKEN.env')

client = discord.Client()

bot_command = '&'
bot_commands = ['help', 'hello']

def low(str):
    return str.lower()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(bot_command):
        commands = str(message.content)[1:]
        parsed = commands.split(" ")

        command = low(parsed[0])
        arguments = list(map(low, parsed[1:]))

        if command not in bot_commands:
            await message.channel.send(f"Invalid command, use {bot_command}help command for help.")
            return 

        print(f"\nAUTHOR: {message.author}")
        print(f"COMMAND: {command} ")
        print(f"ARGUMENTS: {arguments}")
        
        if command == "help":
            await message.channel.send(f'Command List: {bot_commands}')

        if command == "hello":
            author = str(message.author).split("#")
            await message.channel.send(f'Hello, {author[0]}')

        
client.run(os.environ['TOKEN'])