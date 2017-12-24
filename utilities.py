import discord


async def error_embed(msg):
    e = discord.Embed(color=discord.Color.red())
    e.set_author(name="🚫 Something went wrong!")
    e.description = msg
    return e


async def success_embed(msg):
    e = discord.Embed(color=discord.Color.green())
    e.set_author(name="✔️ Success!")
    e.description = msg
    return e


async def wip_embed():
    e = discord.Embed(color=discord.Color.dark_orange())
    e.set_author(name="🛠️ This command is under construction.")
    e.description = "Unfortunately, this command isn't available just yet. Try again at a later date."
    return e
