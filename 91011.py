#import openweathermapy.core as weather
import unicodedata
import youtube_dl
import pyowm
import traceback
import os
import sys
import sqlite3
import discord
from discord.ext import commands
import random
import asyncio
from datetime import datetime
import aiohttp
import json
import requests
import datetime
import time
from bs4 import BeautifulSoup
import ftfy
#from cosmos_sql import PastaSQL

bot = commands.Bot(command_prefix=commands.when_mentioned_or("?"))
bot.remove_command ('help')

@bot.event
async def on_ready():
    print("------------")
    print(" Logged in.")
    print("⭐Bot Ready⭐")
    print("------------")

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
      await bot.send_message(ctx.message.channel, "**:x: | This command is on cooldown, try again later. (╯°□°）╯︵ ┻━┻**")

#    elif isinstance(error, commands.CommandNotFound):
#      await bot.send_message(ctx.message.channel, "**:x: | That command was not found! Type ?help for a list of commands.（￣～￣;）**")

   # elif isinstance(error, commands.InvalidArgument):
      #await bot.send_message(ctx.message.channel, f'**:x: | Invalid argument in command {ctx.command}. (」ﾟﾛﾟ)｣**')

    print('Ignoring exception in command {}:'.format(ctx.command), file = sys.stderr)
    traceback.print_exception(type(error), error, error.__traceback__, file = sys.stderr)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    elif "cosmos" in message.content:
      await bot.send_message(message.channel, (random.choice(["Yes?", "No", "How is that even possible...", "He's an asshole.","\n😎😎😎😎😎😎😎\n👍   I'm so cool!   👍\n💋😏😏😏😏😏💋\n👌🚀🚀🚀🚀🚀👌\n🚗📷📷📷📷📷🚗\n😈😈😈😈😈😈😈", "Sure, ig", "╮(╯▽╰)╭","IMPOSSIBRUUUUU", "( ˘ ³˘)❤", "(づ￣ ³￣)づ", "(っ˘̩╭╮˘̩)っ", "<(⇀‸↼‶)>", "(〜￣△￣)〜", "Take your question, and shove it up the bumof the guy below. 🔽", "Talk to the hand  ✋", "Last night I held a lovely hand,\nIt was so small and neat,\nI thought my heart withjoy would burst\nSo wild was every beat.\n\nNo other hand unto my heart\nCould greater pleasure bring \nThan the one so dear I heldlast night.\nFour Aces and a King"])))
    elif "Cosmos" in message.content:
      await bot.send_message(message.channel, (random.choice(["Yes?", "No", "How is that even possible...", "He's an asshole.","\n😎😎😎😎😎😎😎\n👍I'm so cool!👍\n💋😏😏😏😏😏💋\n👌🚀🚀🚀🚀🚀👌\n🚗📷📷📷📷📷🚗\n😈😈😈😈😈😈😈", "Sure, ig", "╮(╯▽╰)╭","IMPOSSIBRUUUUU", "( ˘ ³˘)❤", "(づ￣ ³￣)づ","(っ˘̩╭╮˘̩)っ", "<(⇀‸↼‶)>", "(〜￣△￣)〜", "Take your question, and shove it up the bumof the guy below. 🔽", "Talk to the hand  ✋", "Last night I helda lovely hand,\nIt was so small and neat,\nI thought my heart withjoy would burst\nSo wild was every beat.\n\nNo other hand unto my heart\nCouldgreater pleasure bring \nThan the one so dear I heldlast night.\nFour Aces and a King"])))
    elif "Rapid" in message.content:
      msg=await bot.send_message(message.channel, "IS GAY")
      await bot.add_reaction(message, "🙇")
      await asyncio.sleep(0.5)
      await bot.edit_message(msg, "**Wait nvm YOU ARE ƪ(˘ᴗ˘)┐**")
      await bot.add_reaction(msg, "✋🏻")
      await bot.add_reaction(msg,"☝️🏻")
    else:
        await bot.process_commands(message)
    
async def my_background_task():
    await bot.wait_until_ready()
    servs = (len(bot.servers))
    users = (len(set(bot.get_all_members())))
    chans = (len(set(bot.get_all_channels())))
    while not bot.is_closed:
        await bot.change_presence(game=discord.Game(name="with {} servers".format(servs)))
        await asyncio.sleep(11.5)
        await bot.change_presence(game=discord.Game(name="with {} users".format(users)))
        await asyncio.sleep(13.5)
        await bot.change_presence(game=discord.Game(name="say ?help"))
        await asyncio.sleep(15.5)
        await bot.change_presence(game=discord.Game(name="?invite | ?help"))
        await asyncio.sleep(17.5)
        await bot.change_presence(game=discord.Game(name="on {} channels".format(chans)))
        await asyncio.sleep(19.0)
        await bot.change_presence(game=discord.Game(name="Prefix = ?"))
        await asyncio.sleep(21.5)
        await bot.change_presence(game=discord.Game(name="Christmas Music | Prefix = ?"))
        await asyncio.sleep(23.5)

#class Pasta:
#
#    def __init__(self, bot):
#        self.bot = bot
#       self.db = PastaSQL()
#        # self.cursor.execute('''CREATE TABLE pasta
#        # (pasta_tag text, pasta_text text, creator_id text, creation_date text,
#        # uses integer, likes integer, dislikes integer)''')
#
#    @bot.command(pass_context=True, aliases=['p'])
#    async def pasta(self, ctx):
#        cmd = await self.extract_cmd_text(ctx, 1)
#        """Call up a user-submitted pasta"""
#        if len(cmd) <= 0:
#            e = await utilities.error_embed("Please state which pasta you would like to identify.")
#            await self.bot.say(embed=e)
#            return
#         if self.db.exists(cmd[0]):
#            pasta_msg = self.db.get(cmd[0])
#            new_uses = int(pasta_msg[1]) + 1
#            self.db.update_uses(new_uses, cmd[0])
#            await self.bot.say(pasta_msg[0])
#            return
#        else:
#            e = await utilities.error_embed("That pasta doesn't exist!")
#            await self.bot.say(embed=e)
#            return
#
#    @bot.command(pass_context=True, aliases=['cp'])
#    async def createpasta(self, ctx):
#        """Make your very own pasta!"""
#        cmd = await self.extract_cmd_text(ctx, 2)
#        if len(cmd) <= 1:
#            e = await utilities.error_embed("I couldn't find any content for this pasta, please specify what you want to make.")
#            await self.bot.say(embed=e)
#            return
#
#        if self.db.exists(cmd[0].lower()):
#            e = await utilities.error_embed("This pasta already exists! Try a different tag.")
#            await self.bot.say(embed=e)
#            return
#        if len(cmd) >= 1:
#            e = discord.Embed()
#            args = (cmd[0].lower(), " ".join(cmd[1:]), ctx.message.author.id, date.today(), 0, 0, 0)
#            self.db.add(args)
#            e.description = "Successfully created new pasta `{}`!".format(cmd[0])
#            await self.bot.say(embed=e)
#            return
#        await self.bot.say("If you're reading this, tell the developer he's an idiot.")
#        return
#
#    @bot.command(pass_context=True, aliases=['ip'])
#   async def infopasta(self, ctx):
#        """Get information about a pasta"""
#        cmd = await self.extract_cmd_text(ctx, 1)
#        if len(cmd) <= 0:
#            e = await utilities.error_embed("**USAGE_REMINDER_HERE**")
#            await self.bot.say(embed=e)
#            return
#        if self.db.exists(cmd[0]):
#            pasta_info = self.db.get_info(cmd[0])
#            e = discord.Embed(color=discord.Color.blue())
#            e.set_author(name=pasta_info[0].upper())
#            e.add_field(name="Created by", value="{} [{}]".format("NYI", pasta_info[2]))
#            e.add_field(name="Date created", value=pasta_info[3])
#            e.add_field(name="Times used", value=pasta_info[4])
#            e.add_field(name="Rating", value="⬆️ {} ⬇️ {}".format(pasta_info[5], pasta_info[6]))'
#            await self.bot.say(embed=e)
#            return
#        e = await utilities.error_embed("**NOT_FOUND**")
#        await self.bot.say(embed=e)
#        return
#
#    @bot.command(pass_context=True, aliases=['lp'])
#    async def lovepasta(self, ctx):
#        """Show your love for a pasta."""
#        await self.vote_pasta(ctx, True)
#
#    @bot.command(pass_context=True, aliases=['hp'])
#    async def hatepasta(self, ctx):
#        """Hate on a pasta. You monster."""
#        await self.vote_pasta(ctx, False)
#        
#    async def vote_pasta(self, ctx, vote):
#        e = await utilities.wip_embed()
#        await self.bot.say(embed=e)
#
#    @bot.command(pass_context=True, aliases=['dp'])
#    async def deletepasta(self, ctx):
#        """Remove a pasta. Accidents happen."""
#        cmd = await self.extract_cmd_text(ctx, 1)
#        author_id = ctx.message.author.id
#
#        if len(cmd) <= 0:
#            e = await utilities.error_embed("Please state which pasta you would like to remove.")
#            await self.bot.say(embed=e)
#            return
#        cmd = cmd[0]
#        if self.db.exists(cmd) is False:
#            e = await utilities.error_embed("This pasta doesn't exist!")
#            await self.bot.say(embed=e)
#            return
#
#        if self.db.pasta_owned(cmd, author_id):
#            self.db.delete(cmd)
#            e = await utilities.success_embed("Deleted pasta `{}`!".format(cmd))
#            await self.bot.say(embed=e)
#            return
#
#        e = await utilities.error_embed("You don't own this pasta.")
#        await self.bot.say(embed=e)
#        return
#    
#   @bot.command(aliases=['pp'])
#    async def poppasta(self):
#        """This command shows the most used pastas"""
#        e = discord.Embed()
#        pastas = self.db.popular()
#        e.title = "Most popular pastas"
#        for item in pastas:
#            if item == pastas[0]:
#                e.add_field(name="👑 " + str(item[0]), value=item[1])
#            else:
#                e.add_field(name=item[0], value=item[1])
#        await self.bot.say(embed=e)
#
#    @bot.command(pass_context=True, aliases=['tp'])
#    async def toppasta(self, ctx):
#        """This command shows the most loved pastas!"""
#        e = await utilities.wip_embed()
#        await self.bot.say(embed=e)
#
#    @bot.command(pass_context=True, aliases=['mp'])
#    async def mypasta(self, ctx):
#        """"""
#        if ctx.message.mentions:
#            user_id = ctx.message.mentions[0].id
#            user_name = ctx.message.mentions[0].name + " doesn't"
#        else:
#            user_id = ctx.message.author.id
#            user_name = "You don't"
#        mp = self.db.get_owned(user_id)
#        # TODO: PAGIFY THIS!!!
#        if len(mp) > 0:
#            ap = []
#            for item in mp:
#                ap.append(item[0])
#            ap.sort()
#            e = discord.Embed()
#            e.description = "`" + "` `".join(ap) + "`"
#            await self.bot.say(embed=e)
#            retu
#        e = await utilities.error_embed("Uh-oh! {} have any pastas!".format(user_name))
#        await self.bot.say(embed=e)
#
#    @bot.command(pass_context=True, aliases=['ep'])
#    async def editpasta(self, ctx):
#        cmd = await self.extract_cmd_text(ctx, 2)
#        user_id = ctx.message.author.id
#        pasta_tag = cmd[0]
#        if len(cmd) < 1:
#            # ERROR
#            return
#        if self.db.exists(pasta_tag) is False:
#            e = await utilities.error_embed("This pasta doesn't exist!")
#            await self.bot.say(embed=e)
#            return
#        if self.db.pasta_owned(pasta_tag, user_id) is False:
#            e = await utilities.error_embed("You don't own this pasta!")
#            await self.bot.say(embed=e)
#            return
#        self.db.update_text(pasta_tag, " ".join(cmd[1:]))
#        e = await utilities.success_embed("Updated pasta!")
#        await self.bot.say(embed=e)
#        return
#
#    @bot.command(pass_context=True, aliases=['sp'])
#    async def searchpasta(self, ctx):
#        cmd = ctx.message.content.split(' ', 2)[1:]
#        if len(cmd) <= 0:
#            # error
#            return
#        if len(cmd) == 1:
#            # self.db.
#            returnreturn
#
#    async def extract_cmd_text(self, ctx, spaces: int):
#        cmd = ctx.message.content.split(" ", spaces)[1:]
#        return cmd
#
#
#
@bot.command(pass_context=True)
async def afk(ctx,*,reason : str):
    user = ctx.message.author
    msg = ctx.message
    afk = open('afk.json').read()
    afk = json.loads(afk)
    afk[user.id] = reason
    afk = json.dumps(afk)
    await bot.say("**:door: | You are now AFK: {}**".format(reason))
    with open('afk.json', 'w') as f:
        f.write(afk)

#async def on_message(message):
#    user = ctx.message.author
#    channel = ctx.message.channel
#    afk = open('afk.json').read()
#    afk = json.loads(afk)
#    if user.id in afk:
#        del afk[user.id]
#        await bot.send_message(channel, "**You are now back from being AFK.**")
#    else:
#        mentions = message.mentions
#        for member in mentions:
#            if member.id in afk:
#                em = discord.Embed(color = 0x0f6bff, description = "That user is currently AFK!")
#                em.add_field(name = "Reason", value = "{}".format(afk[member.id]))
#                em.set_thumbnail(url = member.avatar_url)
#                await bot.send_message(channel, content = "**:door: | {} is AFK!**".format(member.name), embed = em)
#    afk = json.dumps(afk)
#    with open('afk.json') as f:
#        f.write(afk)
#    await bot.process_commands(message)
 
@bot.command()
async def itsrapids():
    rp=discord.Embed(color=0x42b9f4,description="Rapid's sexy color changing color, speaker/clock")
    rp.set_author(name="Rapid's Sexy Speaker/Clock", icon_url="https://cdn.discordapp.com/attachments/385625038444822539/395092752297099264/20171225_225413.jpg")
    rp.set_thumbnail(url="https://cdn.discordapp.com/attachments/385625038444822539/395092752297099264/20171225_225413.jpg")
    rp.set_image(url="https://cdn.discordapp.com/attachments/385625038444822539/395092752297099264/20171225_225413.jpg")
    rp.set_footer(text="Sexy Speaker/Clock", icon_url="https://cdn.discordapp.com/attachments/385625038444822539/395092752297099264/20171225_225413.jpg")
    await bot.say(embed=rp)
    
@bot.command(pass_context=True)
async def nick(ctx, member : discord.Member, *,  name : str):
    if not ctx.message.author.server_permissions.manage_nicknames:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.change_nickname(member, name)
    await bot.say("**:white_check_mark: | Changed {}'s nickname to: `{}`**".format(member.name, name))

@bot.command(pass_context=True)
async def kick(ctx, member : discord.Member, *,  reason: str = ""):
    if not ctx.message.author.server_permissions.kick_members:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.kick(member)
    await bot.send_message(member, "**You were kicked from {}!\nReason: {}\nAction by: {}**".format(ctx.message.server.name, reason, ctx.message.author.name))
    await bot.say("**:white_check_mark: | Kicked {}, reason: `{}`**".format(member.name, reason))

@bot.command(pass_context=True)
async def ban(ctx, member : discord.Member, purge: int = 7):
    if not ctx.message.author.server_permissions.ban_members:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.ban(member, purge)
    await bot.send_message(member, "**You were banned from {}!\nAction by: {}**".format(ctx.message.server.name, ctx.message.author.name))
    await bot.say("**:white_check_mark: | Banned {}.**".format(member.name))

@bot.command(pass_context=True)
async def softban(ctx, member : discord.Member, purge: int = 1):
    if not ctx.message.author.server_permissions.ban_members:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.ban(member, purge)
    await bot.unban(member.server, member)
    await bot.send_message(member, "**You were soft-banned from {}!\nAction by: {}**".format(ctx.message.server.name, ctx.message.author.name))
    await bot.say("**:white_check_mark: | Banned, then un-banned {}.**".format(member.name))

@bot.command(pass_context=True)
async def warn(ctx, member : discord.Member, *, reason: str):
    if not ctx.message.author.server_permissions.kick_members:
        return await bot.say("**:x: | You cannot to do that.**\nReason: **Insufficient Permissions(KickMembers)**")
#    if not user:
#        return await bot.say(ctx.message.author.mention + " Specify a user to warn!")
    await bot.send_message(member, "**You have been warned in {}!\nReason: {}**".format(ctx.message.server.name, reason))
    await bot.say("**:white_check_mark: | Warned {}.**".format(member.name))
    
@bot.command(pass_context=True)
async def addrole(ctx, member : discord.Member, *, role_name: discord.Role):
    if not ctx.message.author.server_permissions.manage_roles:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.add_roles(member, role_name)
    await bot.say("**:white_check_mark: | Added the role {} to {}.**".format(role_name, member.name))

@bot.command(pass_context=True)
async def removerole(ctx, member : discord.Member, *, role_name: discord.Role):
    if not ctx.message.author.server_permissions.manage_roles:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.remove_roles(member, role_name)
    await bot.say("**:white_check_mark: | Removed the role {} from {}.**".format(role_name, member.name))
    
@bot.command(aliases=["ig", "invg"], pass_context=True)
async def invitegenerator(ctx, text : str):
    l=discord.Embed(color=ctx.message.author.color, title="Invite link generator", description="Make sure your message is your bots **Client ID**, eg. `385622427977121813`.")
    l.add_field(name="Here is your link!", value="[Click Me]({})".format("https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8".format(text)))
    await bot.say(embed=l)
        
@bot.command(aliases=["s", "st", "star"], pass_context=True)
async def starboard(ctx,*, message: str):
#    await bot.delete_message(ctx.message) (This is optional. It'll delete the command message if the hash, aswell as this message is removed.)
    embed = discord.Embed(color = 0xffa92a, description = "" + message + "")
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    msg2send = await bot.say(content = "**:star: " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
#    await bot.say("Would you like to publish this quote to the 'quotes' channel? **Yes/No**")
#    mag = await bot.wait_for_message(author = ctx.message.author, content = "Yes")
#    await bot.send_message(bot.get_channel("392833879104290827"), "**:comet: " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**")
    react2 = await bot.send_message(bot.get_channel("392833879104290827"), content = "**:star: " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
    react2 = await bot.send_message(bot.get_channel("393094161764581399"), content = "**:star: " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
    react2 = await bot.send_message(bot.get_channel("393209121928642563"), content = "**:star: " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
    react2 = await bot.send_message(bot.get_channel("393821239032152079"), content = "**:star: " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
    react2 = await bot.send_message(bot.get_channel("393819606344663049"), content = "**:star: " + ctx.message.server.name + " ID: "+ ctx.message.server.id + "**", embed = embed)
#    react2 = await bot.send_message(bot.get_channel(""), content = "**:star: " + ctx.message.server.name + " ID: "+ ctx.message.server.id + "**", embed = embed)
#    react2 = await bot.send_message(bot.get_channel(""), content = "**:star: " + ctx.message.server.name + " ID: "+ ctx.message.server.id + "**", embed = embed)
#    react2 = await bot.send_message(bot.get_channel(""), content = "**:star: " + ctx.message.server.name + " ID: "+ ctx.message.server.id + "**", embed = embed)
    await bot.add_reaction(msg2send, "⭐")
#    await bot.add_reaction(react2, "⭐")
    await bot.say("**:white_check_mark: | " + ctx.message.author.name + ", I've published your message!**")
    
@bot.command(aliases=["suggest", "sug", "sugg"], pass_context=True)
async def suggestion(ctx,*, message: str):
    await bot.delete_message(ctx.message)
    embed = discord.Embed(color = 0xffa92a, description = "" + message + "")
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
#    msg2send = await bot.say(content = "**Suggestion " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
    react2 = await bot.send_message(bot.get_channel("392789385386655754"), content = "**Suggestion from " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
    await bot.add_reaction(react2, "✅")
    await bot.add_reaction(react2, "❌")
    await bot.say("**:white_check_mark: | " + ctx.message.author.name + ", I've sent your suggestion!**\n __{}__".format(message))
    
@bot.command(aliases=["xmas"], pass_context=True)
async def christmas(ctx):
    now = datetime.datetime.utcnow()
    xmas = datetime.datetime(now.year, 12, 25)
    if xmas<now:
        xmas = xmas.replace(year = now.year+1)
    delta=xmas-now
    weeks, remainder = divmod(int(delta.total_seconds()), 604800)
    days, remainder2 = divmod(remainder, 86400)
    hours, remainder3 = divmod(remainder2, 3600)
    minutes, seconds = divmod(remainder3, 60)
    embed = discord.Embed(color = 0x10a542)
    embed.add_field(name = ":christmas_tree: Time left until Christmas :christmas_tree:", value = f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    embed.set_author(name = "Christmas Countdown!", icon_url = ctx.message.author.avatar_url)
    await bot.say(content = "Requested by **" + ctx.message.author.name + "**", embed = embed)

@bot.command(aliases=["hall"], pass_context=True)
async def halloween(ctx):
    now = datetime.datetime.utcnow()
    xmas = datetime.datetime(now.year, 10, 31)
    if xmas<now:
        xmas = xmas.replace(year = now.year+1)
    delta=xmas-now
    weeks, remainder = divmod(int(delta.total_seconds()), 604800)
    days, remainder2 = divmod(remainder, 86400)
    hours, remainder3 = divmod(remainder2, 3600)
    minutes, seconds = divmod(remainder3, 60)
    embed = discord.Embed(color = 0xff5405)
    embed.add_field(name = ":candy: Time left until Halloween :lollipop:", value = f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    embed.set_author(name = "Halloween Countdown!", icon_url = ctx.message.author.avatar_url)
    await bot.say(content = "Requested by **" + ctx.message.author.name + "**", embed = embed)

@bot.command(aliases=["eas"], pass_context=True)
async def easter(ctx):
    now = datetime.datetime.utcnow()
    xmas = datetime.datetime(now.year, 4, 1)
    if xmas<now:
        xmas = xmas.replace(year = now.year+1)
    delta=xmas-now
    weeks, remainder = divmod(int(delta.total_seconds()), 604800)
    days, remainder2 = divmod(remainder, 86400)
    hours, remainder3 = divmod(remainder2, 3600)
    minutes, seconds = divmod(remainder3, 60)
    embed = discord.Embed(color = 0xffe8dd)
    embed.add_field(name = ":chocolate_bar: Time left until Easter :egg:", value = f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    embed.set_author(name = "Easter Countdown!", icon_url = ctx.message.author.avatar_url)
    await bot.say(content = "Requested by **" + ctx.message.author.name + "**", embed = embed)

@bot.command(aliases=["val"], pass_context=True)
async def valentines(ctx):
    now = datetime.datetime.utcnow()
    xmas = datetime.datetime(now.year, 2, 14)
    if xmas<now:
        xmas = xmas.replace(year = now.year+1)
    delta=xmas-now
    weeks, remainder = divmod(int(delta.total_seconds()), 604800)
    days, remainder2 = divmod(remainder, 86400)
    hours, remainder3 = divmod(remainder2, 3600)
    minutes, seconds = divmod(remainder3, 60)
    embed = discord.Embed(color = 0xff0000)
    embed.add_field(name = ":gift_heart: Time left until Valentines Day :ribbon:", value = f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    embed.set_author(name = "Valentines Day Countdown!", icon_url = ctx.message.author.avatar_url)
    await bot.say(content = "Requested by **" + ctx.message.author.name + "**", embed = embed)
    
@bot.command(aliases=["saint"], pass_context=True)
async def saintpatrick(ctx):
    now = datetime.datetime.utcnow()
    xmas = datetime.datetime(now.year, 3, 17)
    if xmas<now:
        xmas = xmas.replace(year = now.year+1)
    delta=xmas-now
    weeks, remainder = divmod(int(delta.total_seconds()), 604800)
    days, remainder2 = divmod(remainder, 86400)
    hours, remainder3 = divmod(remainder2, 3600)
    minutes, seconds = divmod(remainder3, 60)
    embed = discord.Embed(color = 0x56ff5c)
    embed.add_field(name = ":four_leaf_clover: Time left until Saint Patricks Day :crown:", value = f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    embed.set_author(name = "Saint Patricks Day Countdown!", icon_url = ctx.message.author.avatar_url)
    await bot.say(content = "Requested by **" + ctx.message.author.name + "**", embed = embed)
    
@bot.command(pass_context=True)
async def color(ctx, *, color: discord.Colour):
    file = io.BytesIO()
    Image.new('RBG', (200, 90), color.to_rbg()).save(file, format = 'PNG')
    file.seek(0)
    em = discord.Embed(color = color, title = f'Color: {str(color)}')
    em.set_image(url = 'attachment://color.png')
    await bot.say(file = discord.File(file, 'color.png'), embed = em)

@bot.event
async def on_server_join(server, ctx):
    print("I have joined {.name}!".format(server))
    await bot.send_message(server.owner, "Thanks for adding me to you're server! My prefix is `?`, so if you need any help, type `?help` _**Be sure I have all the permissions so that I can function properly!**_\n• Support Server: https://discord.gg/pDvJZEN\n• Owner/Creator: Rapid#0501")
    embed = discord.Embed(color = 0xfffa02)
    embed.add_field(name = "Owner", value = ctx.server.owner)
    await bot.send_message(bot.get_channel("379454585808617472"), content = "**:sparkles: " + ctx.server.name + " ID: " + ctx.server.id + "**", embed = embed)

@bot.command()
async def faq():
    em = discord.Embed(color = 0x8f07ff, title = "Frequently Asked Questions")
    em.add_field(name = "What is the starboard?", value = "My starboard is different, it is a command that allows you to send and view messages from/to any accepted starboard channel. Basically a global chat through Cosmos. Want it in your server? Type `?setup_starboard` to get started!")
    em.add_field(name = "How do you code on mobile?", value = "I code on my Android S7, using an application called Termux, with the editor Nano. Type `?tutTERMUX` on how to do this all yourself.")
    em.add_field(name = "Can I have your code?", value = "No, make your own, and besides, there are many `tut` commands with my bot.")
    em.add_field(name = "How come commands wont work after I use it?", value = "Either insufficient permissions for you or cosmos, or the command is on cooldown.")
    await bot.say(embed = em)
    
@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def pick(ctx):
    pick = discord.Embed(color = 0xf3a8bc, description = "**" + ctx.message.author.name + "**, you've picked {} 🌸".format(random.randint(1, 100)))
    await bot.say(embed = pick)

@bot.command(aliases=["inv", "in", "invent", "mystuff", "stuff"], pass_context=True)
async def inventory(ctx):
    inventory = discord.Embed(color = ctx.message.author.color, description = "\n\nComing soon...\n\n")
    inventory.set_author(name = ctx.message.author.name + "'s Inventory", icon_url = ctx.message.author.avatar_url)
    await bot.say(embed = inventory)
    
@bot.command(pass_context=True)
async def charinfo(ctx, *, characters: str):
    if len(characters) > 10:
        return await bot.say(f"**:x:  |  To many characters. ({len(characters)}/10)**")

    def to_string(c):
        digit = f'{ord(c):x}'
        name = unicodedata.name(c, "**:x:  |  Emoji name not found.**")
        return f'`\\U{digit:>08}`: {name} - {c} \N{EM DASH} <http://www.fileformat.info/info/unicode/char/{digit}>'

    await bot.say("\n".join(map(to_string, characters)))

@bot.command(pass_context=True)
async def invite(ctx):
    await bot.say("**:link: | https://discordapp.com/oauth2/authorize?client_id=385622427977121813&scope=bot&permissions=2146958591**")
    print(ctx.message.author.name + " did invite")

@bot.command(pass_context=True)
async def poll(ctx,*, message: str):
    embed = discord.Embed(color = ctx.message.author.color, timestamp = datetime.datetime.utcnow())
    embed.set_author(name = "Poll", icon_url = ctx.message.author.avatar_url)
    embed.description = (message)
    embed.set_footer(text = ctx.message.author.name)
    x = await bot.say(embed = embed)
    await bot.add_reaction(x, "👍")
    await bot.add_reaction(x, "\U0001f937")
    await bot.add_reaction(x, "👎")

@bot.command(pass_context=True)
async def imdb(ctx, *,query: str = None):
    if not query is None:
        query = query.replace(" ", "+")
        api = "http://www.theimdbapi.org/api/find/movie?title={}".format(query)
        async with aiohttp.ClientSession() as session:
            async with session.get(api) as r:
                response = await r.json()
                try:
                    title = str(response[0]['title'])
                    link = str(response[0]['url']['url'])
                    title = f"[{title}]"f"({link})"
                    year = str(response[0]['year'])
                    genre = str(response[0]['genre']).replace('[','').replace("'","").replace("]","")
                    length1 = str(response[0]['length'])
                    rating = response[0]['content_rating']
                    imdb_rating = response[0]['rating']
                    director = str(response[0]['director'])
                    poster = str(response[0]['poster']['large'])

                    e = discord.Embed(color = ctx.message.author.color, timestamp = datetime.datetime.utcnow())
                    e.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
                    e.add_field(name = ":label: Title", value = title)
                    e.add_field(name = ":calender_spiral: Year", value = year)
                    e.add_field(name = ":performing_arts: Genre", value = genre)
                    e.add_field(name = ":stopwatch: Length", value = length1 +" mins")
                    e.add_field(name = ":bookmark: Rating", value = rating)
                    e.add_field(name = ":heart_decoration: IMDB Rating", value = imdb_rating)
                    e.add_field(name = ":clapper: Director", value = director)
                    e.set_footer(text = "| © Cosmos ")
                    e.set_image(url = poster)
                    await bot.say(embed = e)
                except:
                    await bot.say("**:x: | Couldn't find anything, try again. ┐(￣ヮ￣)┌**")

    else:
        await bot.say("**:x: | Specify a valid search. (」ﾟﾛﾟ)｣**")
        
@bot.command(pass_context=True)
async def quote(ctx):
    quote_url = 'http://quotesondesign.com/api/3.0/api-3.0.json'
    async with aiohttp.ClientSession() as session:
        async with session.get(quote_url) as data:
            quote_req = await data.text()
    quote_text = quote_req.split('$quot;')[1]
    quote_text = ftfy.fix_text(quote_text)
    embed = discord.Embed(color = 0x02ff06, description = quote_text)
    embed.set_author(name = "Random quote", icon_url = ctx.message.author.avatar_url)
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def pun(ctx):
    pun_url = 'http://www.punoftheday.com/cgi-bin/arandompun.pl'
    async with aiohttp.ClientSession() as session:
        async with session.get(pun_url) as data:
            pun_req = await data.text()
    pun_text = pun_req.split('&quot;')[1]
    pun_text = ftfy.fix_text(pun_text)
    embed = discord.Embed(color = 0x02d9ff, description = pun_text)
    embed.set_author(name = "Random pun", icon_url = ctx.message.author.avatar_url)
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def chucknorris(ctx):
    joke_url = 'https://api.chucknorris.io/jokes/random'
    async with aiohttp.ClientSession() as session:
        async with session.get(joke_url) as data:
            joke_data = await data.read()
            joke_json = json.loads(joke_data)
    joke = joke_json['value']
    embed = discord.Embed(color = 0xff6f02, description = joke)
    embed.set_author(name = "Chuck Norris joke", icon_url = ctx.message.author.avatar_url)
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def yomomma(ctx):
    resource = 'http://api.yomomma.info/'
    async with aiohttp.ClientSession() as session:
        async with session.get(resource) as data:
            data = await data.read()
            data = json.loads(data)
    joke = data['joke']
    if not joke.endswith('.'):
        joke += '.'
    embed = discord.Embed(color = 0x8805fc, description = joke)
    embed.set_author(name = "Yo momma joke", icon_url = ctx.message.author.avatar_url)
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def insult(ctx, user: discord.Member = None):
    url = "http://www.insultgenerator.org/"
    with aiohttp.ClientSession() as session:
       async with session.get(url) as resp:
           r = await resp.read()
       resp = Soap(r, 'html.parser')
       if user is not None:
           pre = user.name + ": "
       else:
           pre = ""
       await bot.say(pre + resp.find('div', {'class': 'wrap'}).text.strip("\n"))

#DEVELOPER COMMAND
@bot.command(pass_context=True)
async def dm(ctx, user : discord.Member, *, message: str):
    if ctx.message.author.id == "371001497342836737":
      embed = discord.Embed(color = 0x6691D9, timestamp = datetime.datetime.utcnow(), description = "Message: {}".format(message))
      embed.set_author(name = "Message from Rapid#0501")
      embed.set_footer(text = "| Rapid#0501 ")
      await bot.send_message(destination = user, embed = embed)
      await bot.say("**:white_check_mark: | Message sent to user!**")

#DEVELOPER COMMAND
@bot.command(pass_context=True)
async def edm(ctx, user : discord.Member, *, message: str):
    if ctx.message.author.id == "371001497342836737":
      await bot.send_message("Message: ".format(message), destination = user)
      await bot.say("**:white_check_mark: | Message sent to user!**")

#DEVELOPER COMMAND
@bot.command(pass_context=True)
async def restart(ctx):
    if ctx.message.author.id == "371001497342836737":
      await bot.say("**:ballot_box_with_check:  |  I'll be back!**")
      os.execve(sys.executable, ['Python'] + sys.argv, os.environ)
      
@bot.command()
async def ping():
    pingtime = time.time()
    pingms = await bot.say("Pinging...")
    ping = time.time() - pingtime
    await bot.edit_message(pingms, "**:ping_pong: | Pong!** (%.01f seconds)" % ping)

@bot.command()
async def pong():
    pongtime = time.time()
    pongms = await bot.say("Ponging...")
    pong = time.time() - pongtime
    await bot.edit_message(pongms, "**:ping_pong: | Ping!** (%.01f seconds)" % pong)
    
@bot.command(pass_context=True)
async def rate(ctx,*, thing : str):
    numbers = random.randint(0, 100)
    decimals = random.randint(0, 9)

    if numbers == 100:
        decimals = 0

    await bot.say(f"**:arrows_clockwise: | I'd rate {thing} a `{numbers}.{decimals}/100`**")
    
@bot.command(pass_context=True)
async def reverse(ctx,*, text : str):
    reverse = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
    await bot.say(f'{reverse}')

@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def slots(ctx):
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)

    if (a == b ==c):
        message = f':tada: | You won {ctx.message.author.name}!'
    elif (a == b) or (a == c) or (b == c):
        message = f':hotsprings: | {ctx.message.author.name}, you almost won, 2/3!'
    else:
        message = f':flag_white: | You lost {ctx.message.author.name}.'

    embed = await bot.say(embed=discord.Embed(color=0xffffff, description=f'**:slot_machine: | {ctx.message.author.name} rolled the slots...**'))
    await asyncio.sleep(1.0)
    await bot.edit_message(embed, embed=discord.Embed(color=0xffffff, description=f'**:slot_machine: | {ctx.message.author.name} rolled the slots...\nSpinning...**'))
    await asyncio.sleep(1.0)
    await bot.edit_message(embed, embed=discord.Embed(color=0xffffff, description=f'**:slot_machine: | {ctx.message.author.name} rolled the slots...\nSpinning...\n------{ctx.message.author.name}------**'))
    await asyncio.sleep(1.0)
    await bot.edit_message(embed, embed=discord.Embed(color=0xffffff, description=f'**:slot_machine: | {ctx.message.author.name} rolled the slots...\nSpinning...\n------{ctx.message.author.name}------\n`{a} | {b} | {c}`\n{message}**'))

@bot.command()
async def count():
    co = await bot.say("Beginning...")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "1")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "2")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "3")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "4")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "5")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "6")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "7")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "8")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "9")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "10")
    await bot.say("**:white_check_mark: | Done!**")

@bot.command()
async def virus(user: discord.Member):
    v = await bot.say("Initializing...")
    await asyncio.sleep(3.0)
    await bot.edit_message(v, "[▓                         ] / {WiHb}-virus.exe Packing files.")
    await asyncio.sleep(0.5)
    await bot.edit_message(v, "[▓▓                    ] - {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.7)
    await bot.edit_message(v, "[▓▓▓            ] | {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(1.0)
    await bot.edit_message(v, "[▓▓▓▓        ] / {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.5)
    await bot.edit_message(v, "[▓▓▓▓▓    ] - {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.8)
    await bot.edit_message(v, "[▓▓▓▓▓▓] \ {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(4.0)
    await bot.edit_message(v, "[▓▓▓▓▓▓] - {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.8)
    await bot.edit_message(v, "[▓▓▓▓▓▓] \ {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.5)
    await bot.edit_message(v, "[▓▓▓▓▓▓] - {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(1.2)
    await bot.edit_message(v, "[▓▓▓▓▓▓] / {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(1.0)
    await bot.edit_message(v, "[▓▓▓▓▓▓] - {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.8)
    await bot.edit_message(v, "[▓▓▓▓▓▓] \ {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.8)
    await bot.edit_message(v, "Successfully downloaded virus...")
    await asyncio.sleep(0.5)
    await bot.edit_message(v, "Installing 'WiHb.exe'...")
    await asyncio.sleep(2.0)
    await bot.edit_message(v, "Successfully injected WiHb.exe into **{}**!".format(user.name))

@bot.command(pass_context=True)
async def roles(ctx):
    roles = ctx.message.server.roles
    result = "All of the servers roles are "
    for role in roles:
        embed = discord.Embed(timestamp = datetime.datetime.utcnow(), color = ctx.message.author.color, description = "```" + role.name + "  =  " + role.id + "```\n")
        embed.set_author(name = "All the server roles")
        embed.set_footer(text = "| © Cosmos ")
    await bot.say(embed = embed)
    
@bot.command(pass_context=True)
async def emojis(ctx):
    emojis = ctx.message.server.emojis
    result = "All of the servers emojis are "
    for emoji in emojis:
        result += "```" + emoji.name + "```"

#DEVELOPER COMMAND
@bot.command(pass_context=True, aliases=["setl", "sl"])
async def setlistening(ctx, *, text):
    if ctx.message.author.id == "371001497342836737":
      await bot.change_presence(game = discord.Game(name="%s"% text, type = 2))
      await bot.say("**:white_check_mark: | Done!**")

#DEVELOPER COMMAND
@bot.command(pass_context=True, aliases=["setw", "sw"])
async def setwatching(ctx, *, text):
    if ctx.message.author.id == "371001497342836737":
      await bot.change_presence(game = discord.Game(name="%s"% text, type = 3))
      await bot.say("**:white_check_mark: | Done!**")

#DEVELOPER COMMAND
@bot.command(pass_context=True, aliases=["sets", "ss"])
async def setstream(ctx, *, text):
    if ctx.message.author.id == "371001497342836737":
      await bot.change_presence(game = discord.Game(name="%s"% text, type = 1, url = "https://www.twitch.tv/"))
      await bot.say("**:white_check_mark: | Done!**")
      
#DEVELOLER COMMAND
@bot.command(pass_context=True, aliases=["setg", "sg"])
async def setgame(ctx, *, text):
    if ctx.message.author.id == "371001497342836737":
      game = discord.Game(name="%s"% text)
      await bot.change_status(game)
      await bot.say("**:ballot_box_with_check:  |  Done!**")

@bot.command(aliases=["salt"], pass_context=True)
async def salty(ctx):
    embed = discord.Embed(color = 0xffffff, title = "SOMEONE IS SAAALLTYY!")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/385625038444822539/388167280896376836/giphy-1.gif")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/385625038444822539/388167280896376836/giphy-1.gif")
    await bot.say(embed = embed)

#DEVELOPER COMMAND
@bot.command(pass_context=True)
async def stop(ctx):
    if ctx.message.author.id == "371001497342836737":
      await bot.say("**:white_check_mark: | Shutting down**")
#      st = discord.Embed(color = 0xff0000, description = "<:BOT:392049308016574474>  |  Shutting down...", timestamp = datetime.datetime.utcnow())
#      st.set_author(name = "[SHUTDOWN]", icon_url = ctx.message.author.avatar_url)
#      st.set_footer(text = "| Task request by {} ".format(ctx.message.author.name))
#      await bot.say(embed = st)
      await asyncio.sleep(1)
      await bot.close()
      
@bot.command()
async def info():
    embed = discord.Embed(color = 0x6691D9, timestamp = datetime.datetime.utcnow(), title = "Cosmos Info", description = "Cosmos is a bot made only by Rapid, no more than a bit of help and some command examples from others. It is coded on an Android S7 on an application called Termux, by Rapid")
    embed.set_author(name = "All bot info and statistics", icon_url = "https://cdn.discordapp.com/attachments/379454585808617472/389255356636987394/20171206_140705.jpg")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/379454585808617472/389255356636987394/20171206_140705.jpg")
    embed.add_field(name = "Owner/Creator :spy:", value = "Rapid#0501")
#    embed.add_field(namr = "Uptime :timer:", value = uptime)
    embed.add_field(name = "Running on <:Python:390560559113961472>", value = "Python Discord.py\nOn Termux, Nano\n(Soon on PC)")
#    embed.add_field(name = "Memory :package:", value = f"{ramUsage:.2f} MB")
#    embed.add_field(name = "CUP :desktop:", value = cpu_text)
    embed.add_field(name = "Population :star:", value = "Servers: **{}".format(len(bot.servers)) + "**\n" + "Members: **{}".format(len(set(bot.get_all_members()))) + "**\n" + "Members Online:  **{}".format(sum(1 for m in bot.get_all_members() if m.status != discord.Status.offline)) + "**\n" + "Channels: **{}".format(len(set(bot.get_all_channels()))) + "**\n" + "Emojis: **{}".format(len(set(bot.get_all_emojis()))) + "**\n" + "Total Commands: **97**")
#    embed.add_field(name = "Channels :radio:", value = (len(set(bot.get_all_channels()))))
#    embed.add_field(name = "Members :bow:", value = (len(set(bot.get_all_members()))))
#    embed.add_field(name = "Members :bow:", value = members)
#    embed.add_field(name = "Emojis :star:", value = (len(set(bot.get_all_emojis()))))
#    embed.add_field(name = "Version :inbox_tray:", value = "4.8")
    embed.add_field(name = "Links :link:", value = "[Support Server]({})" .format("https://discord.gg/pDvJZEN") + "\n" + "[Invite Me]({})".format("https://discordapp.com/oauth2/authorize?client_id=385622427977121813&scope=bot&permissions=2146958591"))
    embed.set_footer(text = "| © Cosmos ", icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
    await bot.say(embed = embed)
    
@bot.command()
async def drake():
    embed = discord.Embed(color = 0x075dba, title = "Hotline bling")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/382331380656242702/382550019711959040/drake.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/382331380656242702/382550019711959040/drake.gif")
    await bot.say(embed = embed)

@bot.command()
async def coinflip():
    choice = random.randint(1,2)
    if choice == 1:
       await bot.say("**:hear_no_evil:  |  Heads!**")
    if choice == 2:
       await bot.say("**:monkey:  |  Tails!**")

@bot.command()
async def potatos():
    embed = discord.Embed(color = 0xffd670, title = "Potatos")
    embed.add_field(name = "Create a password:", value = "potato")
    embed.add_field(name = "Password must be atleast 8 characters long.", value = "boiled potato")
    embed.add_field(name = "Password must have atleast 1 number.", value = "1 boiled potato")
    embed.add_field(name = "Password cannot have a space.", value = "50FUCKINGpotatos")
    embed.add_field(name = "Password cannot have capitals.", value = "IfYouDoNotGiveMeAccess,RightNowIWillShove50FuckingPotatosUpUrAss")
    embed.add_field(name = "Password can only have letters & numbers.", value = "IWillShove50FuckingPotatosUpUrAssRightNowIfYouDontGiveMeAccess")
    embed.add_field(name = "Incorrect Password.", value = "FuckYou")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/382331380656242702/384143018145611777/Potatoes_PNG_Clipart.png")
    await bot.say(embed = embed)
    
@bot.command()
async def servercount():
    await bot.say(len(bot.servers))

@bot.command()
async def channelcount():
    await bot.say(len(bot.servers))

@bot.command()
async def membercount():
    await bot.say(len(set(bot.get_all_members())))

@bot.command()
async def emojicount():
    await bot.say(len(set(bot.get_all_emojis())))

@bot.command(pass_context=True)
async def say(ctx,*, message: str):
    await bot.delete_message(ctx.message)
    await bot.say(message)

@bot.command(pass_context=True)
async def embedsay(ctx,*, message: str):
    await bot.delete_message(ctx.message)
    embed = discord.Embed(color = ctx.message.author.color)
    embed.description = (message)
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def avatar(ctx, member : discord.Member):
    av=discord.Embed(color=member.color)
    av.set_author(icon_url=member.avatar_url, name="Avatar for {}".format(member.name))
    av.set_image(url=member.avatar_url)
    await bot.say(content="Requested by **{}**".format(ctx.message.author.name), embed=av)
    
@bot.command()
async def choose(*choices : str):
    await bot.say(random.choice(choices))

@bot.command()
async def add(left,right):
    answer=int(left) + int(right)
    await bot.say("**:ledger: | That equals: {}**".format(answer))

@bot.command()
async def subtract(left,right):
    answer=int(left) - int(right)
    await bot.say("**:ledger: | That equals: {}**".format(answer))

@bot.command()
async def divide(left,right):
    answer=int(left) / int(right)
    await bot.say("**:ledger: | That equals: {}**".format(answer))

@bot.command()
async def multiply(left,right):
    answer=int(left) * int(right)
    await bot.say("**:ledger: | That equals: {}**".format(answer))

@bot.command()
async def roll():
    await bot.say(random.choice(["**:game_die:  |  You rolled a 1!**", "**:game_die:  |  You rolled a 2!**", "**:game_die:  |  You rolled a 3!**", "**:game_die:  |  You rolled a 4!**", "**:game_die:  |  You rolled a 5!**", "**:game_die:  |  You rolled a 6!**"]))

@bot.command(name='is')
async def _is(left, right):
    left = int(left)
    right = int(right)
    if int(left) > int(right):
        await bot.say("**:ledger: | {} is greater than {}**".format(left, right))
    elif int(left) < int(right):
        await bot.say("**:ledger: | {} is less than {}**".format(left, right))
    
@bot.command()
async def power(left,right):
    answer=int(left) ** int(right)
    await bot.say("**:ledger: | That equals: {}**".format(answer))
    
@bot.command(pass_context=True)
async def kill(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = (random.choice(["Call **911,** {} just attempted suicide".format(ctx.message.author.name),
                                                            "{} just tried to kill themself!!!".format(ctx.message.author.name),
                                                            "Prep the stone, {} just died.... :(".format(ctx.message.author.name),
                                                            "WE NEED AN ABULANCE!!! {} MIGHT HAVE JUST DIED".format(ctx.message.author.name),
                                                            "{} decided to leave us, he'll be missed.".format(ctx.message.author.name)])), color = ctx.message.author.color)
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "**{}** was killed by **{}** ".format(member.name, ctx.message.author.name), color = ctx.message.author.color)
        await bot.say(embed = embed)

@bot.command(pass_context=True)
async def hug(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = (random.choice(["So **sad,** {} just hugged themself lmao".format(ctx.message.author.name),
                                                            "{} just hugged em' self".format(ctx.message.author.name),
                                                            "{} didn't wanna hug anyone else, no love for us... :(".format(ctx.message.author.name),
                                                            "{} looks like a good hugger, hey, could you give us some o' dat? :o".format(ctx.message.author.name),
                                                            "{} hugged no one but his hallow shell".format(ctx.message.author.name)])), color = ctx.message.author.color)
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "Adorable, **{}** hugged **{}** ".format(ctx.message.author.name, member.name), color = ctx.message.author.color)
        await bot.say(embed = embed)

@bot.command(pass_context=True)
async def kiss(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = (random.choice(["AHHAHA {} kissed themself... what a shame".format(ctx.message.author.name),
                                                            "{} just kissed em' self".format(ctx.message.author.name),
                                                            "Kisses! Oh wait nevermind, just for {}".format(ctx.message.author.name),
                                                            "{} kissed\n\n\n\n\n\n\n\n\n\n\n\n\n\n THEMSELF".format(ctx.message.author.name),
                                                            "{} kissed his own body, ew".format(ctx.message.author.name)])), color = ctx.message.author.color)
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "**{}** kissed **{}**, aweeeee ".format(ctx.message.author.name, member.name), color = ctx.message.author.color)
        await bot.say(embed = embed)

@bot.command(pass_context=True)
async def punch(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = (random.choice(["Erm {} punched... themself??".format(ctx.message.author.name),
                                                            "{} just flippin' punched em' self".format(ctx.message.author.name),
                                                            "~PUNCH~ watchout, {} is on a punching rampage".format(ctx.message.author.name),
                                                            "{} punched out his eye, physco much".format(ctx.message.author.name),
                                                            "{} just punched themself... lol".format(ctx.message.author.name)])), color = ctx.message.author.color)
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "**{}** just punched **{}**, dayuuuumm ".format(ctx.message.author.name, member.name), color = ctx.message.author.color)
        await bot.say(embed = embed)

@bot.command(pass_context=True)
async def slap(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = (random.choice(["Ouch, {} slapped themself".format(ctx.message.author.name),
                                                            "What in Trap Nation is {} doing?! They slapped themself, lmao".format(ctx.message.author.name),
                                                            "Slaps for everyone! Oh wait, you're all in luck, I guess just {}".format(ctx.message.author.name),
                                                            "{} slapped himself right across his on FaCcEee".format(ctx.message.author.name),
                                                            "{} slapped {}".format(ctx.message.author.name, ctx.message.author.name)])), color = ctx.message.author.color)
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "Watchout guys... **{}** slapped **{}** for what appears to be no reason... ouch ".format(ctx.message.author.name, member.name), color = ctx.message.author.color)
        await bot.say(embed = embed)

@bot.command(pass_context=True)
async def beatup(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = (random.choice(["AHHAHA {} beat themself up into a ball... what a shame".format(ctx.message.author.name),
                                                            "{} smh, what a weirdo".format(ctx.message.author.name),
                                                            "{} beat up his own damn body, what is up with his head".format(ctx.message.author.name),
                                                            "{} is your head on right... or?".format(ctx.message.author.name),
                                                            "{} is beating himself ;D".format(ctx.message.author.name)])), color = ctx.message.author.color)
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "Damn, **{}** took a hard beating from this dood named **{}**, aweeeee ".format(member.name, ctx.message.author.name), color = ctx.message.author.color)
        await bot.say(embed = embed)
        
@bot.command(name="8ball")
async def _ball():
    await bot.say(random.choice([":8ball:  |  Obviously", ":8ball:  | I'm not sure", ":8ball:  |  Yes", ":8ball:  |  No", ":8ball:  |  It is certain", ":8ball:  |  No shit", ":8ball:  |  Ofcourse", ":8ball:  |  ...", ":8ball:  |  To be honest, who would even know", ":8ball:  |  It is believed so", ":8ball:  |  It's best you do not talk about it"]))

@bot.command()
async def shoot():
    await bot.say(random.choice([":basketball:  |  Wow you got it stuck... you throw a light wrist m8", ":basketball:  |  Dayum you got in... nice", ":basketball:  |  Wow, garbage, you need practice", ":basketball:  |  Toilet spin, close one pal", ":basketball:  |  Good try"]))

@bot.command()
async def dicklength():
    await bot.say(random.choice([":straight_ruler:  |  8==D 3 inches... small asf", ":straight_ruler:  |  8=========D 10 inches... jesus wtf, your definately gettin\' laid", ":straight_ruler:  |  8D bro...", ":straight_ruler:  |  8========================D 27 INCHES....... bro your a GOD", ":straight_ruler:  |  8====D 5 inches... typical asf"]))

@bot.command()
async def amicool():
    await bot.say(random.choice([":wastebasket:  |  Nothing...", ":tada:  |  Cool!", ":skull_crossbones:  |  Your... well um... you ain\'t cool... sorry...", ":hole:  |  No words to describe you"]))
    
@bot.command()
async def starterpack():
    embed = discord.Embed(color = 0xee42f4, title = "Starter Pack")
    embed.set_author(name = "Look at this dood")
    embed.set_image(url = (random.choice(["https://cdn.discordapp.com/attachments/385625038444822539/388910981008457731/the-i-think-im-a-cool-math-teacher-starter-pack-6231496.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388911006706958341/images.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388911006706958336/OA0dCuI.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388911005633347585/7a7ba29b1d24b610659ffbe7f62de0d6--laughing-so-hard-funny-photos.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388911853922942978/images-1.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388911898835288064/126.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916557167984640/2117_ball-is-life.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388912371831406602/images-2.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913784686641152/tough-white-guy.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913784686641153/5z2vrt8amkpx.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913784003100683/slutty-white-girl-starter-pack-pink-victorias-secret-tag-one-15815796.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913784003100682/22-and-date-a-14-year-old.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913783550246912/84588610.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913735864942593/cea.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913734804045835/Annoyingmiddleschoolerstarterpack_0921e3_6313403.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916555192336384/he-latino-gangster-starter-pack-sc-blsnapz-12339278.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916557662781440/images-6.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916555640995840/4748276d39148c755d7e99f383678dec.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916554022256653/1xuaa2.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916554022256650/Km4Dbjj.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916501425553409/images-4.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916501425553408/1d2d0a1c28aa87b9778348f0b99320f3.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916499965804544/3df9723ebff5d734ec782f422c5e7e0a.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916500502937610/85508353.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916498988662785/Weveallmetthispersonwhenilivedinport_0bd170_5558718.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916498988662784/images-5.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916497575313409/beauty-pageants.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916497575313408/435.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916496190930945/3bfff573ef4201b307d66cb33198facf.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927711957090306/the-high-school-latina-starter-pack-follow--all-mexicans-8419447.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927711126749184/22581923_139077836723395_6788546199054974976_n.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927711957090304/spoton_starter_packs_for_different_types_of_people_640_19.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927710501535744/LedeCoffee_starterKits_JustMoved_wwstaff.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927709696360451/4aa3fe75067c724676044697f577631c--packing-humor-college-memes.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927690322739200/7da4d2987b02dfa987b0f9bbd189e3da.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927689790193665/rich-white-boy-starter-pack-hoodxsavage-if-this-aint-true-11759588.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927689790193664/424_im-a-white-boy-who-thinks-hes-ghetto.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927688737292289/images-7.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927688196358154/aKgOzob_700b.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927688737292288/funny_starter_packs_21.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927687718338560/female-asian-college-student-starter-pack-5848263.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927631812460545/the-school-bus-driver-starter-pack-how-true-is-thistag-9739067.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927632550526976/2016-emo-girl-starter-pack-fuck-me-daddy-american-send-6291714.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927687718338561/azVDwEp_700b.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927631812460544/23-8.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927630314962954/Screenshot_20171208-222713.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927631195635712/the-recently-divorced-middle-class-dad-starter-pack-dark-brown-9980877.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927628452560896/yBjC8VUr.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927629073580032/aOyMgLR_700b.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916496190930944/starter3.jpg"])))
    await bot.say(embed = embed)    
    
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    if user.id == "371001497342836737":
      embed = discord.Embed(color = ctx.message.author.color, description = "Game Status: {}".format(user.game))
      embed.add_field(name = "NAME", value = user.name)
      embed.add_field(name = "DISCORD ID", value = format(user.id))
      embed.add_field(name = "STATUS", value = format(user.status))
      embed.add_field(name = "BADGES", value = "<:dev:393838678943989761>")
      embed.set_footer(text = "Account made at {}".format(user.created_at))
      embed.set_thumbnail(url = format(user.avatar_url))
      await bot.say(content = "Information on **" + user.name + "#" + user.discriminator + "**", embed = embed)
    elif user.id in["371001497342836737", "389819327039406080"]:
      embed = discord.Embed(color = ctx.message.author.color, description = "Game Status: {}".format(user.game))
      embed.add_field(name = "NAME", value = user.name)
      embed.add_field(name = "DISCORD ID", value = format(user.id))
      embed.add_field(name = "STATUS", value = format(user.status))
      embed.add_field(name = "BADGES", value = "<:dev:393838678943989761>")
      embed.set_footer(text = "Account made at {}".format(user.created_at))
      embed.set_thumbnail(url = format(user.avatar_url))
      await bot.say(content = "Information on **" + user.name + "#" + user.discriminator + "**", embed = embed)
    if not user.id in["371001497342836737", "389819327039406080"]:
      embed = discord.Embed(color = ctx.message.author.color, description = "Game Status: {}".format(user.game))
      embed.add_field(name = "NAME", value = user.name)
#    embed.add_field(name = "NICKNAME", value = format(user.nick))
      embed.add_field(name = "DISCORD ID", value = format(user.id))
      embed.add_field(name = "STATUS", value = format(user.status))
#    embed.add_field(name = "PLAYING", value = format (user.game))
#    embed.add_field(name = "HIGHEST ROLE", value = format(user.top_role))
#    embed.add_field(name = "JOINED AT", value = format(user.joined_at))
#    embed.add_field(name = "JOIN POSITION", value = sorted(ctx.server.members, key=lambda m: m.joined_at).index(user) + 1)
      embed.add_field(name = "BADGES", value = "`None`")
      embed.set_footer(text = "Account made at {}".format(user.created_at))
      embed.set_thumbnail(url = format(user.avatar_url))
      await bot.say(content = "Information on **" + user.name + "#" + user.discriminator + "**", embed = embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(color = 0xffffff)
    embed.set_author(name = "The server info")
    embed.add_field(name = "SERVER NAME", value = ctx.message.server.name)
    embed.add_field(name = "SERVER ID", value = ctx.message.server.id)
    embed.add_field(name = "OWNER", value = ctx.message.server.owner)
    embed.add_field(name = "SERVER SIZE (BIG)", value = ctx.message.server.large)
    embed.add_field(name = "VERIFICATION LEVEL", value = ctx.message.server.verification_level)
    embed.add_field(name = "REGION", value = ctx.message.server.region)
    embed.add_field(name = "MEMBERS", value = ctx.message.server.member_count)
    embed.add_field(name = "SERVER MADE AT", value = ctx.message.server.created_at)
    embed.set_thumbnail(url = ctx.message.server.icon_url)
    await bot.say(embed = embed)
    
@bot.command(pass_context=True)
async def roleinfo(ctx, *,role: discord.Role):
    embed = discord.Embed(color = role.color)
    embed.set_author(name = "The role info")
    embed.add_field(name = "ROLE NAME", value = format(role.name))
    embed.add_field(name = "ROLE ID", value = format(role.id))
    embed.add_field(name = "FOR SERVER", value = format(role.server))
    embed.add_field(name = "HOIST", value = format(role.hoist))
    embed.add_field(name = "ROLE POSITION", value = format(role.position))
    embed.add_field(name = "MENTIONABLE ROLE", value = format(role.mentionable))
    embed.add_field(name = "ROLE CREATED AT", value = format(role.created_at))
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def channelinfo(ctx, *,channel: discord.Channel):
    embed = discord.Embed(color = ctx.message.author.color)
    embed.set_author(name = "The channel info")
    embed.add_field(name = "CHANNEL NAME", value = format(channel.name))
    embed.add_field(name = "CHANNEL ID", value = format(channel.id))
    embed.add_field(name = "FOR SERVER", value = format(channel.server))
    embed.add_field(name = "TOPIC", value = format(channel.topic))
    embed.add_field(name = "CHANNEL POSITION", value = (channel.position))
    embed.add_field(name = "CHANNEL TYPE", value = format(channel.type))
    embed.add_field(name = "CHANNEL CREATED AT", value = format(channel.created_at))
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def emojiinfo(ctx, *,emoji: discord.Emoji):
    embed = discord.Embed(color = ctx.message.author.color)
    embed.set_author(name = "The emoji info")
    embed.add_field(name = "EMOJI NAME", value = format(emoji.name))
    embed.add_field(name = "EMOJI ID", value = format(emoji.id))
    embed.add_field(name = "FOR SERVER", value = format(emoji.server))
    embed.add_field(name = "COLONS", value = format(emoji.require_colons))
    embed.add_field(name = "EMOJI URL", value = format(emoji.url))
    embed.add_field(name = "EMOJI CREATED AT", value = format(emoji.created_at))
    embed.set_thumbnail(url = emoji.url)
    await bot.say(embed = embed)

@bot.command()
async def urband(*msg):

    word = ' '.join(msg)
    api = "http://api.urbandictionary.com/v0/define"
    async with aiohttp.ClientSession() as session:
        async with session.get(api, params={'term': word}) as r:
            response = await r.json()
        if len(response["list"]) == 0:
            x = "Could not find that word!"
            embed=discord.Embed(title='Error', color=0xFF0000)
            embed.description = x
            await bot.say(embed=embed)

        else:
                embed = discord.Embed(title = 'Urban Dictionary - ' + word, color = 0x8f07ff)
                embed.description = response['list'][0]['definition']
                embed.set_thumbnail(url = "https://images-ext-2.discordapp.net/external/B4lcjSHEDA8RcuizSOAdc92ithHovZT6WkRAX-da_6o/https/erisbot.com/assets/emojis/urbandictionary.png")
                embed.add_field(name = "Examples:", value = response['list'][0]["example"][:1000])
                embed.set_footer(text = "Tags: " + ', '.join(response['tags']))
                await bot.say(embed = embed)

@bot.command(pass_context=True)
async def cat():
    r = requests.get('https://random.cat/meow')
    cat = str(r.json()['file'])
    embed = discord.Embed(title = "Meow.", description = "Here is your cat.", color = 0x00ff44)
   # embed.set_thumbnail(url = cat)
    embed.set_author(name = "Random cat")
    embed.set_image(url = cat)
    embed.set_footer(text = "| © Cosmos |")
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def dog():
    api = "https://api.thedogapi.co.uk/v2/dog.php"
    async with aiohttp.ClientSession() as session:
        async with session.get(api) as r:
            if r.status == 200:
                response = await r.json()
                embed = discord.Embed(title = "Woof.", description = "Here is your dog.", color = 0x00ff44)
                embed.set_author(name = "Random dog")
                embed.set_image(url = response['data'][0]["url"])
                embed.set_footer(text = "| © Cosmos |")
                await bot.say(embed = embed)

@bot.command(pass_context=True)
async def servers(ctx):
    if ctx.message.author.id == "371001497342836737":
      x = ', '.join([str(server) for server in bot.servers])
      y = len(bot.servers)
      embed = discord.Embed(description = "```json\n" + x + "```", color = 0xff0000, timestamp = datetime.datetime.utcnow())
      embed.set_author(name = "All the servers I'm in: " + str(y), icon_url = "https://cdn.discordapp.com/attachments/379454585808617472/389255356636987394/20171206_140705.jpg")
      embed.set_footer(text = "| © Cosmos ", icon_url = "https://cdn.discordapp.com/attachments/379454585808617472/389255356636987394/20171206_140705.jpg")
      await bot.say(embed = embed)
      
oo = 14
@bot.command()
async def tutPING():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple **Ping** command.\n```@bot.command()\nasync def ping():\n    await bot.say('Pong!')```")
    embed.set_author(name = "Example 1 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutBASICBOT():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description ="Simple **Bot setup.**\n```import discord\n\nbot = commands.Bot(command_prefix='PREFIX')\n\n@bot.event\nasync def on_ready():\n    print('I'm Ready!')\n\n@bot.command()\nasync def ping():\n    await bot.say('Pong!')\n\nbot.run('TOKEN')```")
    embed.set_author(name = "Example 2 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutCOINFLIP():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple **Coinflip** command.```@bot.command()\nasync def coinflip():\n    choice = random.randint(1,2)\n    if choice == 1:\n       await bot.say('**:hear_no_evil:  |  Heads!**')\n    if choice == 2:\n       await bot.say('**:monkey:  |  Tails!**')```")
    embed.set_author(name = "Example 3 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutSAY():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple **Say** command, deletes your command message, and the bot repeats your message.```@bot.command(pass_context=True)\nasync def say(ctx,*, message: str):\n    await bot.delete_message(ctx.message)\n    await bot.say(message)```")
    embed.set_author(name = "Example 4 of {}".format(oo))
    await bot.say(embed = embed)

#@bot.command()
#async def tutONSERVERJOIN():
#    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "An easy to make **on_server_join** event.```@bot.event\nasync def on_server_join(server):\n    print('I have joined {.name}!'.format(server))\n    await bot.send_message(server.owner, 'ANY MESSAGE TO SEND TO THE OWNER OF THE SERVER Y$
#    embed.set_author(name = "Example 5 of {}".format(oo))
#    await bot.say(embed = embed)

#@bot.command()
#async def tutONMESSAGE():
#    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "An easy to make **on_message** event. (random message)```@bot.event\nasync def on_message(message):\n    if 'test' in message.content:\n      await bot.send_message(message.channel, (random.choice(['Yes?', 'No', 'Sure', 'lol'])))\n  $
#    embed.set_author(name = "Example 6 of {}".format(oo))
#    await bot.say(embed = embed)

@bot.command()
async def tutTYPES():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "All of the presence types you can set for different status types.\nType 0: `Game (playing)`\nType 1: `Stream (streaming)`\nType 2: `Listen (listening to)`\nType 3: `Watch (watching)`")
    embed.set_author(name = "Example 7 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutSERVERS():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple command showing how many servers thr bot is on.```@bot.command()\nasync def servercount():\n    await bot.say(len(bot.servers))```")
    embed.set_author(name = "Example 8 of {}".format(oo))
    await bot.say(embed = embed)
    
@bot.command()
async def tutCHANNELS():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple command showing all the channels the bot can see.```@bot.command()\nasync def channelcount():\n    await bot.say(len(bot.servers))```")
    embed.set_author(name = "Example 9 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutMEMBERS():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple command showing all members the bot can see.```@bot.command()\nasync def membercount():\n    await bot.say(len(set(bot.get_all_members())))```")
    embed.set_author(name = "Example 10 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutEMOJIS():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple command showing all the custom emojis the bot can see.```@bot.command()\nasync def emojicount():\n    await bot.say(len(set(bot.get_all_emojis())))```")
    embed.set_author(name = "Example 11 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutERRORHANDLER():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple **command error handler**```@bot.event\nasync def on_command_error(error, ctx):\n    if isinstance(error, commands.CommandOnCooldown):\n      await bot.send_message(ctx.message.channel, 'This command is on cooldown.')\n\n    elif isinstance(error, commands.CommandNotFound):\n      await bot.send_message(ctx.message.channel, 'This command was not found.')```\nMake the **cooldown** command```@bot.command()\n@commands.cooldown(1, 30, commands.BucketType.user)\nasync def blah():\n    await bot.say('Wasgud :D')```\n__**Definitions**__:book:\n`1, 30` - **1** command every **30** seconds.")
    embed.set_author(name = "Example 12 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutSETGAME():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple command for setting the bots **playing status** on command```@bot.command(pass_context=True, aliases=['setg', 'sg'])\nasync def setgame(ctx, *, text):\n    if ctx.message.author.id == 'YOUR ID': < this will make the command only accessible by you.\n      game = discord.Game(name='%s'% text)\n      await bot.change_status(game)\n      await bot.say('Done!')```")
    embed.set_author(name = "Example 13 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutTERMUX():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple setup for coding on Android, with Termux.\n\nPart 1\nWhen you first open Termux, you need to do a few things:\n1. `pkg install nano`\n2. `pkg install python or nodejs`\n3. `pkg install git`\n4. `pip install discord`\n`Nano` let's you edit or create files. `Python` or `NodeJS`  determines a what languages you can use to code. You can use as many as you want, but each file can obviously only use 1. Now, install `Hackers Keyabord` app from the playstore so you can use specific functions to actually code.\n\nPart 2\nNow, to begin coding type, `nano (filename).py` or `nano bot.js` e.g. `nano bot.py`. Now, you can import discord with `import discord` and begin your code! If you need an example for starters, type **?tutBASICBOT**, and I'll send some code;)\n\nPart 3\nTo use functions and save, etc...\nWhen your in your code open `Hackers Keyboard`, Then press `ctrl` > `x` `(savename)` > `y`\nTo cut text(by lines) do `ctrl` > `k`\nTo show line numbers do `esc` > `ctrl` > `#`\n\n(PYTHON) - To run your bot type `python (filename).py`\n(NODE) - To run your bot type `node (filename).js`")
    embed.set_author(name = "Example 14 of {}".format(oo))
    await bot.say(embed = embed)
    
@bot.command(pass_context=True)
async def tutinfo(ctx):
    embed = discord.Embed(title = "Cosmos Commands", color = 0xfffa02, timestamp = datetime.datetime.utcnow())
    embed.set_author(name = "Information on Cosmos Examples", icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
    embed.add_field(name = "What is it?", value = "Cosmos examples are simple pieces of code that are made by Rapid(me), and set as a command, for people that need help, examples or ideas of commands/code.")
    embed.add_field(name = "What kind of code/language is it?", value = "The code is using the Async library of the language Python, discord.py.")
    embed.add_field(name = "Can I request my code to be here?", value = "Soon, Rapid will be working on a command that allows you to direct message him, for any purposes. Following, a system for your code sent to Rapid to be debated on, and published to a command similar to 'tut', but more so like 'communitytut'.")
    embed.set_footer(text = "| © Cosmos ", icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
    await bot.say(embed = embed)
    
@bot.command(pass_context=True)
async def setup_starboard(ctx):
    if not ctx.message.author.server_permissions.administrator:
      return await bot.say("**:x: | You cannot do that, get the owner or administrator to do this.**")
    await bot.create_channel(ctx.message.server, 'starboard', type=discord.ChannelType.text)
    await bot.say("**:white_check_mark: | I've made the channel, now IN THAT CHANNEL type `?config_starboardid`**")
#    await bot.wait_for_message(author=ctx.message.author, content = "?config_starboardid")
#   await bot.send_message(bot.get_channel("379454585808617472"), "**New starboard request - ID: " + ctx.message.channel.id + "\n" + "Name: " + ctx.message.channel.name + "Server Name: " + ctx.message.server.name + "\nRequester: " + ctx.message.author.name + "**"
#    await bot.say("**:white_check_mark: | Done, soon you can now view the starboard in your server, make sure no one can actually type, except Cosmos, ofcourse. (be patient)**")

@bot.command(pass_context=True)
async def config_starboardid(ctx):
    if not ctx.message.author.server_permissions.administrator:
      return await bot.say("**:x: | You cannot do that, get the owner or administrator to do this.**")
    embed = discord.Embed(color = 0xffffff, title = "Starboard Request!") #, description = "Starboard ID: {}".format(message))
    embed.add_field(name = "Server", value = ctx.message.server.name)
    embed.add_field(name = "Server ID", value = ctx.message.server.id)
    embed.add_field(name = "Server User Count", value = ctx.message.server.member_count)
    embed.add_field(name = "Server Owner", value = ctx.message.server.owner)
    embed.add_field(name = "Channel Name", value = ctx.message.channel.name)
    embed.add_field(name = "Channel ID", value = ctx.message.channel.id)
    embed.add_field(name = "Requester", value = ctx.message.author.name)
    embed.set_thumbnail(url = ctx.message.server.icon_url)
    await bot.send_message(bot.get_channel("379454585808617472"), content = "**Channel ID: " + ctx.message.channel.id + "**", embed = embed)
    await bot.say("**:white_check_mark: | Starboard request sent, now make sure no one can actually type in this channel.\nREMINDER:  I will only accept this request if the channel name is 'starboard'**")

@bot.command(pass_context=True)
async def widentext(ctx,*, text : str):
    output = ""
    for character in text:
            if '!' <= character <= '~':
                    output += chr(ord(character) + 65248)
            else:
                    output += character
    wt=discord.Embed(color=0xff00aa, description=output)
    await bot.say(embed=wt)

@bot.command(pass_context=True)
async def fingers(ctx,*, text : str):
    fr=discord.Embed(color=0xff00aa, description=":point_right::skin-tone-2: {} :point_left::skin-tone-2:".format(text))
    await bot.say(embed=fr)

@bot.command(pass_context=True)
async def scramble(ctx,*, text : str):
    txtdata = list(' '.join(text))
    random.shuffle(txtdata)
    txt = ''.join(txtdata)
    sc=discord.Embed(color=0xff00aa, description="{}".format(txt))
    await bot.say(embed=sc)
    
@bot.command(pass_context=True)
async def emojify(ctx,*, text : str):
    output = ""
    for character in text:
            if 'a' <= character.lower() <= 'z':
                    output += ":regional_indicator_{}:".format(character.lower())
            elif '0' <= character <= '9':
                    output += ":{}:".format(clients.inflect_engine.number_to_words(int(character)))
            else:
                    output += character
    try:
            emjfy=discord.Embed(color=0xff00aa, description=output)
            await bot.say(embed=emjfy)
    except discord.errors.HTTPException:
            pass
    
@bot.command(pass_context=True, aliases=["feedback", "messsgedev", "fb"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def msgdev(ctx, *, pmessage : str = None):
    invite = await bot.create_invite(ctx.message.channel, max_uses = 0)
    bot_owner = 371001497342836737
    dev = bot.get_user_info(bot_owner)

    if pmessage == None:
         await bot.say("**:x: | Provide a message. ヽ( ´¬`)ノ")
    else:
            msg = "User: {}\nServer: {}\nFeedBack: {}\nServer Invite: {}".format(ctx.message.author, ctx.message.server, pmessage, invite.url)
            embed = discord.Embed(title = "Invite to {} server!".format(ctx.message.server), color = ctx.message.author.color, url = "{}".format(invite.url), description = "Feedback: {}".format(pmessage), timestamp = datetime.datetime.utcnow())
            embed.set_thumbnail(url = "{}".format(ctx.message.author.avatar_url))
            embed.set_author(name = "{} sent:".format(ctx.message.author), icon_url = "{}".format(ctx.message.author.avatar_url))
            await bot.send_message(bot.get_channel("379454585808617472"), embed = embed)
            embed = discord.Embed(description = "I have sent **Rapid#0501** your message!", color = 0x00ff00)
            embed.set_footer(text = "| © Origami Tobiichi |")
            await bot.say(content = "**:green_book: | {}**".format(ctx.message.server), embed = embed)
    
@bot.command(pass_context=True)
@commands.cooldown(1, 3600, commands.BucketType.user)
async def advert(ctx):
    await bot.say("I'll be asking a series of questions...")
    await asyncio.sleep(5.0)
    await bot.say("What is your server name?")
    name = await bot.wait_for_message(timeout = 30.0, author = ctx.message.author)
    await bot.say("How many **humans** are in your server?")
    humans = await bot.wait_for_message(timeout = 30.0, author = ctx.message.author)
    await bot.say("Provide a **detailed** description of your server.")
    desc = await bot.wait_for_message(timeout = 30.0, author = ctx.message.author)
    await bot.say("Finally, provide a **permanent** invite link.")
    inv = await bot.wait_for_message(timeout = 30.0, author = ctx.message.author)
#    await bot.purge_from(ctx.message.channel, limit = 8)
    await bot.say("**:white_check_mark: | Your advertisement has been entered!**")
    embed = discord.Embed(title = "New Advert!", color = ctx.message.author.color, description = "**" + ctx.message.author.name + "#" + ctx.message.author.discriminator + " ID: " + ctx.message.author.id + "**", timestamp = datetime.datetime.utcnow())
    embed.add_field(name = "Server Name", value = name.content)
    embed.add_field(name = "Humans", value = humans.content)
    embed.add_field(name = "Description", value = desc.content)
    embed.add_field(name = "Invite", value = inv.content)
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    embed.set_footer(text = "Advert")
    await bot.send_message(bot.get_channel("393669769649192960"), embed = embed)
    await bot.send_message(ctx.message.author, "Thanks for your advertisement! If you'd like to check it out you can join Cosmos's Hub at https://discord.gg/pDvJZEN")
    
@bot.command(pass_context=True)
async def rtfm(ctx, msg : str):
    em=discord.Embed(color=0x6691D9, description="[{}]({})".format(msg, "http://discordpy.readthedocs.io/en/latest/api.html#discord.Client.{}".format(msg)))
    em.set_author(name="Client.{}".format(msg), icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=em)

@bot.command()
async def rtfm_rewrite():
    await bot.say("**:mag_right: | http://discordpy.readthedocs.io/en/rewrite/**")

@bot.command()
async def rtfm_async():
    await bot.say("**:mag_right: | http://discordpy.readthedocs.io/en/async/**")
    
cmds = "97"
@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
   user2send = ctx.message.author
   embed = discord.Embed(title = "Cosmos Commands", color = 0x6691D9, timestamp = datetime.datetime.utcnow(), description = "Cosmos's prefix is `?` If you need specific help on a command type `?help_<command>`")
   embed.set_author(name = '{} total commands'.format(cmds), icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
   embed.add_field(name = "Core Commands", value = "`help` | `info` | `invite` |  `msgdev` | `faq` | `betatesters` | `suggestion`")
   embed.add_field(name = "Utility Commands", value = "`invitegenerator` | `setup_starboard` | `charinfo` | `starboard` | `poll` | `serverinfo` | `channelinfo` | `userinfo` | `emojiinfo` | `roleinfo` | `roles` | `avatar` | `urband` | `advert` | `timer`")
   embed.add_field(name = "Developer Commands", value = "`dm` | `announce` | `stop` | `servers` | `setwatching` | `setgame` | `setlistening` | `setstream`")
   embed.add_field(name = "Administrative Commands", value = "`kick` | `ban` | `softban` | `mute` | `warn` | `gbans` | `addrole` | `removerole`")
   embed.add_field(name = "Fun Commands", value = "`virus` | `ping` | `pong` | `rate` | `starterpack` | `coinflip` | `roll` | `choose` | `8ball` | `kill` | `hug` | `kiss` | `punch` | `slap` | `beatup` | `shoot` | `dicklength` | `amicool` | `dog` | `cat` | `drake` | `salty` | `pun` | `yomomma` | `chucknorris` | `count` | `potatos` | `pick`")
   embed.add_field(name = "Miscellaneous Commands", value ="`embedsay` | `say` | `emojify` | `scramble` | `widentext` | `fingers` | `randomcommand` | `itsrapids` | `is` | `add` | `divide` | `multiply` | `subtract` | `power` |  `christmas` | `halloween` | `easter` | `saintpatrick` | `valentines`")
   embed.add_field(name = "MiniGame Commands", value = "`war` | `slots`")
   embed.add_field(name = "Read the manual Commands", value = "`rtfm` | `rtfm_async` | `rtfm_rewrite`")
   embed.add_field(name = "Discord.py Async HowTo's", value = "`tutBASICBOT` | `tutPING` | `tutSAY` | `tutCOINFLIP` | `tutONMESSAGE` | `tutONSERVERJOIN` | `tutTYPES` | `tutSERVERS` | `tutMEMBERS` | `tutCHANNELS` | `tutEMOJIS` | `tutERRORHANDLER` | `tutSETGAME` | `tutTERMUX`")
   embed.set_footer(text = "| © Cosmos ", icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
   embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
   await bot.send_message(user2send, embed = embed)

   await bot.say("**:white_check_mark: | I've sent you all my commands!**")

@bot.command()
async def help_rtfm():
    h = discord.Embed(title = "Rtfm Command", color = 0x6691D9, description = "Sends the corrosponding link to your message")
    h.add_field(name = "Usage", value = "`?rtfm <event_message>`")
    h.add_field(name = "Note", value = "I don't allow spaces for this because they're not needed, like `rtfm wait_for_message`, pease don't requests fake/dumb links")
    await bot.say(embed = h)
    
@bot.command()
async def help_virus():
    h = discord.Embed(title = "Virus Command", color = 0x6691D9, description = "Inject a virus into someone")
    h.add_field(name = "Usage", value = "`?virus <@user>`")
    h.add_field(name = "Note", value = "Don't overuse this")
    await bot.say(embed = h)

@bot.command()
async def help_add():
    h = discord.Embed(title = "Add Command", color = 0x6691D9, description = "Adds 2 values together")
    h.add_field(name = "Usage", value = "`?add <number1> <number2>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_subtract():
    h = discord.Embed(title = "Subtract Command", color = 0x6691D9, description = "Subtract a value from another")
    h.add_field(name = "Usage", value = "`?subtract <number1> <number2>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_divide():
    h = discord.Embed(title = "Divide Command", color = 0x6691D9, description = "Groups a value into another")
    h.add_field(name = "Usage", value = "`?divide <number1> <number2>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_multiply():
    h = discord.Embed(title = "Multiply Command", color = 0x6691D9, description = "Multiplies a value by another")
    h.add_field(name = "Usage", value = "`?multiply <number1> <number2>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_is():
    h = discord.Embed(title = "Is Command", color = 0x6691D9, description = "Determines if a value is or is not greater than another")
    h.add_field(name = "Usage", value = "`?is <number1> <number2>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_power():
    h = discord.Embed(title = "Power Command", color = 0x6691D9, description = "Multiplies the value by the amount of the second value")
    h.add_field(name = "Usage", value = "`?power <number1> <number2>`")
    h.add_field(name = "Note", value = "Empty...")
    
@bot.command()
async def help_rate():
    h = discord.Embed(title = "Rate Command", color = 0x6691D9, description = "Rates your message out of 100")
    h.add_field(name = "Usage", value = "`?rate <message>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_war():
    h = discord.Embed(title = "War Command", color = 0x6691D9, description = "Begin a simple card game")
    h.add_field(name = "Usage", value = "`?war`")
    h.add_field(name = "Note", value = "Don't overuse this")
    await bot.say(embed = h)
    
@bot.command()
async def help_invitegenerator():
    h = discord.Embed(title = "Invite Generator Command", color = 0x6691D9, description = "Create an instant bot authorization link")
    h.add_field(name = "Usage", value = "`?invitegenerator <client id>`")
    h.add_field(name = "Note", value = "Avoid this command if the server doesn't allow advertisements/links/invites")
    await bot.say(embed = h)
    
@bot.command()
async def help_slots():
    h = discord.Embed(title = "Slots Command", color = 0x6691D9, description = "Spins the slot machine")
    h.add_field(name = "Usage", value = "`?slots`")
    h.add_field(name = "Note", value = "Don't overuse this")
    await bot.say(embed = h)
    
@bot.command()
async def help_timer():
    h = discord.Embed(title = "Timer Command", color = 0x6691D9, description = "Sets a timer for you")
    h.add_field(name = "Usage", value = "`?timer <seconds>`")
    h.add_field(name = "Note", value = "This command has a cooldown of a minute to prevent spam")
    await bot.say(embed = h)
    
@bot.command()
async def help_setup_starboard():
    h = discord.Embed(title = "Setup_starboard Command", color = 0x6691D9, description = "Begins a setup wizard for the beta starboard")
    h.add_field(name = "Usage", value = "`?setup_starboard <the rest is interactive setup>`")
    h.add_field(name = "Note", value = "PLEASE make sure you follow all steps correctly")
    await bot.say(embed = h)

@bot.command()
async def help_msgdev():
    h = discord.Embed(title = "Msgdev Command", color = 0x6691D9, description = "Sends your message to Rapid")
    h.add_field(name = "Usage", value = "`?msgdev <message>`")
    h.add_field(name = "Note", value = "This command has a 2 minute cooldown")
    await bot.say(embed = h)

@bot.command()
async def help_advert():
    h = discord.Embed(title = "Advert Command", color = 0x6691D9, description = "Allows you to advertise your server in Cosmos's Hub")
    h.add_field(name = "Usage", value = "`?advert <the rest is interactive setup>`")
    h.add_field(name = "Note", value = "Please do not abuse this command, the command has a 1 hour cooldown for each person")
    await bot.say(embed = h)

@bot.command()
async def help_suggestion():
    h = discord.Embed(title = "Suggestion Command", color = 0x6691D9, description = "Sends your suggestion to Cosmos's Hub")
    h.add_field(name = "Usage", value = "`?suggestion <message>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_charinfo():
    h = discord.Embed(title = "Charinfo Command", color = 0x6691D9, description = "Displays info on any character")
    h.add_field(name = "Usage", value = "`?charinfo <emoji> or <character>`")
    h.add_field(name = "Note", value = "Custom emotes are not supported, max of 10 characters p/c")
    await bot.say(embed = h)

@bot.command()
async def help_starboard():
    h = discord.Embed(title = "Starboard Command", color = 0x6691D9, description = "Posts a message in any starboard channel that Rapid sets (ask Rapid#0501 for more info)")
    h.add_field(name = "Usage", value = "`?starboard <message>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_poll():
    h = discord.Embed(title = "Poll Command", color = 0x6691D9, description = "Begins a simple poll, embeds your message and adds 3 reactions")
    h.add_field(name = "Usage", value = "`?poll <message>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_serverinfo():
    h = discord.Embed(title = "Serverinfo Command", color = 0x6691D9, description = "Displays info on the server")
    h.add_field(name = "Usage", value = "`?serverinfo`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_channelinfo():
    h = discord.Embed(title = "Channelinfo Command", color = 0x6691D9, description = "Displays info on the given channel")
    h.add_field(name = "Usage", value = "`?channelinfo <#channel>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_userinfo():
    h = discord.Embed(title = "Userinfo Command", color = 0x6691D9, description = "Displays info on the given user")
    h.add_field(name = "Usage", value = "`?userinfo <@user>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_emojiinfo():
    h = discord.Embed(title = "Emojiinfo Command", color = 0x6691D9, description = "Displays info on the given emoji")
    h.add_field(name = "Usage", value = "`?emojiinfo <:emote:> or <name> or <just the emoji>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_roleinfo():
    h = discord.Embed(title = "Roleinfo Command", color = 0x6691D9, description = "Displays info on the given role")
    h.add_field(name = "Usage", value = "`?roleinfo <@role> or <name>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_say():
    h = discord.Embed(title = "Say Command", color = 0x6691D9, description = "Makes the bot repeat your message")
    h.add_field(name = "Usage", value = "`?say <message>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_embedsay():
    h = discord.Embed(title = "Embedsay Command", color = 0x6691D9, description = "Makes the bot repeat your message in an embed")
    h.add_field(name = "Usage", value = "`?embedsay <message>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_urband():
    h = discord.Embed(title = "Urband Command", color = 0x6691D9, description = "Defines the given word with the Urban Dictionary API")
    h.add_field(name = "Usage", value = "`?urband <word>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_kick():
    h = discord.Embed(title = "Kick Command", color = 0x6691D9, description = "Kicks the given user")
    h.add_field(name = "Usage", value = "`?kick <@user> or <username>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_ban():
    h = discord.Embed(title = "Ban Command", color = 0x6691D9, description = "Bans the given user")
    h.add_field(name = "Usage", value = "`?ban <@user> or <username>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_warn():
    h = discord.Embed(title = "Say Command", color = 0x6691D9, description = "Warns the given user with a reason")
    h.add_field(name = "Usage", value = "`?warn <@user> <reason>`")
    h.add_field(name = "Note", value = "Disabled (WIP)")
    await bot.say(embed = h)
    
@bot.command()
async def help_gbans():
    h = discord.Embed(title = "Gbans Command", color = 0x6691D9, description = "Fetches all banned members in the server")
    h.add_field(name = "Usage", value = "`?gbans`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_mute():
    h = discord.Embed(title = "Mute Command", color = 0x6691D9, description = "Mutes the given user for any amount of time")
    h.add_field(name = "Usage", value = "`?mute <@user> or <username> <time>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_softban():
    h = discord.Embed(title = "Mute Command", color = 0x6691D9, description = "Bans, then unbans the member")
    h.add_field(name = "Usage", value = "`?softban <@user> or <username>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_addrole():
    h = discord.Embed(title = "Addrole Command", color = 0x6691D9, description = "Adds the given role to a member")
    h.add_field(name = "Usage", value = "`?addrole <@user> or <username> then <@role> or <rolename>`")
    h.add_field(name = "Note", value = "No mentions needed")
    await bot.say(embed = h)
    
@bot.command()
async def help_removerole():
    h = discord.Embed(title = "Removerole Command", color = 0x6691D9, description = "Removes the given role from a member")
    h.add_field(name = "Usage", value = "`?removerole <@user> or <username> then <@role> or <rolename>`")
    h.add_field(name = "Note", value = "No mentions needed")
    await bot.say(embed = h)
    
@bot.command()
async def help_choose():
    h = discord.Embed(title = "Choose Command", color = 0x6691D9, description = "Makes the bot choose between any options")
    h.add_field(name = "Usage", value = "`?choose <option1> | <option2> | <option3>`")
    h.add_field(name = "Note", value = "The bot will sometimes choose the seperator")
    await bot.say(embed = h)

@bot.command()
async def help_8ball():
    h = discord.Embed(title = "8ball Command", color = 0x6691D9, description = "Ask the bot a question for an answer")
    h.add_field(name = "Usage", value = "`?8ball <question>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def betatesters():
    em = discord.Embed(color = 0x0596ff, title = "Beta Testers", description = "**Rapid#0501\nDankXXlol#6659**")
    await bot.say(embed = em)
    
@bot.command(aliases=["getbans", "bans"], pass_context=True)
async def gbans(ctx):
    if not ctx.message.author.server_permissions.administrator:
      return await bot.say("**:x: | Insufficient permissions.**")
    x = await bot.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    if x == None:
      embed = discord.Embed(title = "Banned Members for {}".format(ctx.message.server.name), description = "No bans, squeeky clean! ;)", color = 0x596ff)
      await bot.say(embed = embed)
    else:
        embed = discord.Embed(title = "Banned Members for {}".format(ctx.message.server.name), description = x, color = 0x596ff)
        await bot.say(embed = embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def timer(ctx, seconds : int):
    e = discord.Embed(title = "Set a timer", color = 0x8f07ff, description = ":timer: | {}, I'll remind you in {} seconds.".format(ctx.message.author.name, seconds))
    e.set_thumbnail(url = ctx.message.author.avatar_url)
    await bot.say(embed = e)
    await asyncio.sleep(seconds)
    await bot.say("**:timer: | {} seconds have passed, {}.**".format(seconds, ctx.message.author.mention))
    
@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def war(ctx):
    cards = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
    member = ctx.message.author.name
    player = random.randint(2, 14)
    dealer = random.randint(2, 14)
    embed = await bot.say(embed=discord.Embed(color=0x49bcff, description="**:shield: | Shuffling the cards...**"))
    await asyncio.sleep(1.0)
    await bot.edit_message(embed, embed=discord.Embed(color=0x49bcff, description="**:shield: | Shuffling the cards...\nDealing...**"))
    await asyncio.sleep(1.0)
    await bot.edit_message(embed, embed=discord.Embed(color=0x49bcff, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**'))
    if int(player) > int(dealer):
        await asyncio.sleep(1.0)
        await bot.edit_message(embed, embed=discord.Embed(color=0x84ba74, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}-----**\n`Player: ' + cards[player] + '`\n`Dealer: ' + cards[dealer] + '`\n**:tada: | You won {}!**'.format(ctx.message.author.name)))
    elif int(player) < int(dealer):
        await asyncio.sleep(1.0)
        await bot.edit_message(embed, embed=discord.Embed(color=0xde0036, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**\n`Player: ' +cards[player] + '`\n`Dealer: ' + cards[dealer] + '`\n**:skull_crossbones: | You lost {}.**'.format(ctx.message.author.name)))
    else:
        await asyncio.sleep(1.0)
        player2 = random.randint(2, 14)
        player3 = random.randint(2, 14)
        player4 = random.randint(2, 14)
        dealer2 = random.randint(2, 14)
        dealer3 = random.randint(2, 14)
        dealer4 = random.randint(2, 14)
        if int(player4) > int(dealer4):
            await asyncio.sleep(1.0)
            await bot.edit_message(embed, embed=discord.Embed(color=0x84ba74, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**\n`Player: ' + cards[player] + '`, ' + cards[player2] + ', ' + cards[player3] + ', `**Deciding Card: **' + cards[player4] + '`\nDealer: ' + cards[dealer] + '`, ' + cards[dealer2] + ', ' + cards[dealer3] + ', `**Deciding Card: **' + cards[dealer4] + '`\n**:tada: | You won {}!**'.format(ctx.message.author.name)))
        elif int(player4) < int(dealer4):
            await asyncio.sleep(1.0)
            await bot.edit_message(embed, embed=discord.Embed(color=0xde0036, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**\n`Player: ' +cards[player] + '`, ' + cards[player2] + ', ' + cards[player3] + ', `**Deciding Card: **' + cards[player4] + '`\nDealer: ' +cards[dealer] + '`, ' + cards[dealer2] + ', ' + cards[dealer3] + ', `**Deciding Card: **' + cards[dealer4] + '`\n**:skull_crossbones: | You lost {}.**'.format(ctx.message.author.name)))
        else:
            await asyncio.sleep(1.0)
            await bot.edit_message(embed, embed=discord.Embed(color=0xffc627, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**\n`Player: ' +cards[player] + '`, ' + cards[player2] + ', ' + cards[player3] + ', `**Deciding Card: **' + cards[player4] + '`\nDealer: ' +cards[dealer] + '`, ' + cards[dealer2] + ', ' + cards[dealer3] + ', `**Deciding Card: **' + cards[dealer4] + '`\n**:crossed_swords: | {}, it is a tie!**'.format(ctx.message.author.name)))

@bot.command()
async def randomcommand():
    rc=discord.Embed(color=0x8f07ff, title="Random Command", description="**?{}**".format(random.choice(tuple(set(command.name for command in bot.commands.values())))))
    rc.add_field(name="About", value="Commands you see here, and not in the **help** command, are for testing.")
    await bot.say(embed=rc)
            
bot.loop.create_task(my_background_task())
if not os.environ.get('TOKEN'):
    print("no token found!")
bot.run(os.environ.get('TOKEN').strip('"'))
