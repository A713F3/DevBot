from discord import Embed

def help_embed():
    help_message = discord.Embed(title="How to use the DevBot :question:", description="- Useful Commands :rocket:-", color=0x000006)
    help_message.add_field(name="&help", value="- Display all commands")
    help_message.add_field(name="&hello", value="- Says hello to the user")
    help_message.add_field(name="&github add (username)", value="- Adds Github profile to accounts channel")
    help_message.add_field(name="&github del", value="- Deletes Github profile from accounts channel")
    help_message.add_field(name="&linkedin add (account link)", value="- Adds LinkedIn profile to accounts channel")
    help_message.add_field(name="&linkedin del", value="- Deletes LinkedIn profile from accounts channel")
    help_message.set_image(url="https://github.com/A713F3/DevBot/blob/master/devbot.png?raw=true")

    return help_message

def welcome_embed():
    welcome_message = discord.Embed(title=":coffee: Grab a cup of coffee and start coding...", description=":mag_right: **Hint:** try &help", color=0x000006)
    return welcome_message