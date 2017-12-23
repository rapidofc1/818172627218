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

bot = commands.Bot(command_prefix=commands.when_mentioned_or("?"))
bot.remove_command ('help')

async def on_command_completion(ctx):
    bot.commands_used[ctx.command.name] += 1
    await asyncio.sleep(5.0)
    try:
        await bot.message.delete()
    except Exceptation as e:
        print(e)

def is_owner_check(message):
    return  message.author.id == "371001497342836737"

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))

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

    elif isinstance(error, commands.CommandNotFound):
      await bot.send_message(ctx.message.channel, "**:x: | That command was not found! Type ?help for a list of commands.（￣～￣;）**")

   # elif isinstance(error, commands.InvalidArgument):
      #await bot.send_message(ctx.message.channel, f'**:x: | Invalid argument in command {ctx.command}. (」ﾟﾛﾟ)｣**')

    print('Ignoring exception in command {}:'.format(ctx.command), file = sys.stderr)
    traceback.print_exception(type(error), error, error.__traceback__, file = sys.stderr)

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
async def rip(ctx, user: discord.Member):
    user = user.name
    await bot.say("<http://ripme.xyz/{}>".format(user.replace(" ", "%20")))

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
async def pong(ctx):
    pongtime = time.time()
    pongms = await bot.say("Ponging...")
    pong = time.time() - pongtime
    await bot.edit_message(pongms, "**:ping_pong: | Ping!** (%.01f seconds)" % pong)
    
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

@bot.command(pass_context=True)
async def warn(ctx, user: discord.Member, *, reason: str):
    if not ctx.message.author.server_permissions.kick_members:
        return await bot.say("**:x: | You cannot to do that.**\nReason: **Insufficient Permissions(KickMembers)**")
    if not user:
        return await bot.say(ctx.message.author.mention + " Specify a user to warn!")
    embed = discord.Embed(color = 0xffffff, title = "You've been warned!", description = "Reason: {}".format(reason))
    await bot.send_message(destination = user, embed = embed)
    await bot.say("**:white_check_mark: | Warned {}**".format(user.name))

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
    embed.add_field(name = "Population :star:", value = "Servers: **{}".format(len(bot.servers)) + "**\n" + "Members: **{}".format(len(set(bot.get_all_members()))) + "**\n" + "Members Online:  **{}".format(sum(1 for m in bot.get_all_members() if m.status != discord.Status.offline)) + "**\n" + "Channels: **{}".format(len(set(bot.get_all_channels()))) + "**\n" + "Emojis: **{}".format(len(set(bot.get_all_emojis()))) + "**\n" + "Total Commands: **67**")
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

@bot.command()
async def choose(*choices : str):
    await bot.say(random.choice(choices))

@bot.command()
async def add(left : int, right : int):
    await bot.say(left + right)

@bot.command()
async def roll():
    await bot.say(random.choice(["**:game_die:  |  You rolled a 1!**", "**:game_die:  |  You rolled a 2!**", "**:game_die:  |  You rolled a 3!**", "**:game_die:  |  You rolled a 4!**", "**:game_die:  |  You rolled a 5!**", "**:game_die:  |  You rolled a 6!**"]))
    
@bot.command(pass_context=True)
async def kill(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = "Call **911**", color = 0xff0000)
        #embed.set_image(url = (random.choice(["http://4.bp.blogspot.com/-FL6mKTZOk94/UBb_9EuAYNI/AAAAAAAAOco/JWsTlyInMeQ/s400/Jean+Reno.gif", "https://cdn.discordapp.com/attachments/385625038444822539/393441155636789248/giphy-5.gif", "https://cdn.discordapp.com/attachments/385625038444822539/393441425477337108/200w-3.$
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "**{}** Was killed by **{}** ".format(member.name, ctx.message.author.name),color = ctx.message.author.color)
        #embed.set_image(url = (random.choice(["https://discordapp.com/oauth2/authorize?client_id=385622427977121813&scope=bot&permissions=2146958591", "https://cdn.discordapp.com/attachments/385625038444822539/393056123311226901/giphy-3.gif", "https://cdn.discordapp.com/attachments/385625038444822539/39305612331122690$
        await bot.say(embed = embed)

@bot.command(pass_context=True)
async def hug(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = "**{}** hugged themself".format(ctx.message.author.name), color = 0xff0000)
        #embed.set_image(url = (random.choice([])))
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "**{}** hugged **{}** ".format(ctx.message.author.name, member.name),color = ctx.message.author.color)
        #embed.set_image(url = (random.choice(["https://cdn.discordapp.com/attachments/379454585808617472/393445391229648898/giphy_s-1.gif", "https://cdn.discordapp.com/attachments/379454585808617472/393445390680326145/giphy-16.gif", "https://cdn.discordapp.com/attachments/379454585808617472/393445390164164609/giphy-17$
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
async def kick():
    await bot.say("**:x: | That command is disabled for now.**")

@bot.command()
async def ban():
    await bot.say("**:x: | That command is disabled for now.**")

@bot.command()
async def mute():
    await bot.say("**:x: | That command is disabled for now.**")
    
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
                embed = discord.Embed(title = 'Urban Dictionary - ' + word, color = 0xf75959)
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

#@bot.command()
#async def tutBASICBOT():
#    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description ="Simple **Bot setup.**\n```import discord\n\nbot = commands.Bot(command_prefix='PREFIX')\n\n@bot.event\nasync def on_ready():\n    print('I'm Ready!')\n\n@bot.command()\nasync def ping():\n    await bot.say('Pong!')\n\nbot.run('TOKEN')$
#    embed.set_author(name = "Example 2 of {}".format(oo))
#    await bot.say(embed = embed)

#@bot.command()
#async def tutCOINFLIP():
#    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple **Coinflip** command.```@bot.command()\nasync def coinflip():\n    choice = random.randint(1,2)\n    if choice == 1:\n       await bot.say('**:hear_no_evil:  |  Heads!**')\n    if choice == 2:\n       await bot.say('**:monkey:$
#    embed.set_author(name = "Example 3 of {}".format(oo))
#    await bot.say(embed = embed)

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

#@bot.command()
#async def tutERRORHANDLER():
    #embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple **command error handler**```@bot.event\nasync def on_command_error(error, ctx):\n    if isinstance(error, commands.CommandOnCooldown):\n      await bot.send_message(ctx.message.channel, 'This command is on cooldown.')\n\n    e$
    #embed.set_author(name = "Example 12 of {}".format(oo))
    #await bot.say(embed = embed)

#@bot.command()
#async def tutSETGAME():
    #embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple command for setting the bots **playing status** on command```@bot.command(pass_context=True, aliases=['setg', 'sg'])\nasync def setgame(ctx, *, text):\n    if ctx.message.author.id == 'YOUR ID': < this will make the command on$
    #embed.set_author(name = "Example 13 of {}".format(oo))
    #await bot.say(embed = embed)

#@bot.command()
#async def tutTERMUX():
    #embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple setup for coding on Android, with Termux.\nPart 1\nWhen you first open Termux, you need to do a few things:\n1. `pkg install nano`\n2. `pkg install python or nodejs`\n3. `pkg install git`\n4. `pip install discord`\n`Nano` let'$
    #embed.set_author(name = "Example 14 of {}".format(oo))
    #await bot.say(embed = embed)
    
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
    
cmds = "72"
@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
   user2send = ctx.message.author
   embed = discord.Embed(title = "Cosmos Commands", color = 0x6691D9, timestamp = datetime.datetime.utcnow(), description = "Cosmos's prefix is `?` If you need specific help on a command type `?help_<command>`")
   embed.set_author(name = '{} total commands'.format(cmds), icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
   embed.add_field(name = ":star2: LIMITED :star2:", value = "`christmas`")
   embed.add_field(name = "Core Commands", value = "`help` | `info` | `invite` | `suggestion` | `msgdev` | `setup_starboard` | `faq` | `betatesters`")
   embed.add_field(name = "Utility Commands", value = "`charinfo` | `starboard` | `poll` | `serverinfo` | `channelinfo` | `userinfo` | `emojiinfo` | `roleinfo` | `roles` | `say` | `embedsay` | `urband` | `advert`")
   embed.add_field(name = "Developer Commands", value = "`dm` | `announce` | `stop` | `rapidify` | `servers` | `setwatching` | `setgame` | `setlistening` | `setstream`")
   embed.add_field(name = "Administrative Commands", value = "`kick` | `ban` | `mute` | `warn`")
   embed.add_field(name = "Fun Commands", value = "`virus` | `ping` | `pong` | `starterpack` | `coinflip` | `roll` | `choose` | `8ball` | `kill` | `hug` | `shoot` | `dicklength` | `amicool` | `dog` | `cat` | `add` | `drake` | `salty` | `pun` | `yomomma` | `chucknorris` | `count` | `potatos` | `pick`")
   embed.add_field(name = "Discord.py Async HowTo's", value = "`tutBASICBOT` | `tutPING` | `tutSAY` | `tutCOINFLIP` | `tutONMESSAGE` | `tutONSERVERJOIN` | `tutTYPES` | `tutSERVERS` | `tutMEMBERS` | `tutCHANNELS` | `tutEMOJIS` | `tutERRORHANDLER` | `tutSETGAME` | `tutTERMUX`")
   embed.set_footer(text = "| © Cosmos ", icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
   embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
   await bot.send_message(user2send, embed = embed)

   await bot.say("**:white_check_mark: | I've sent you all my commands!**")

@bot.command()
async def help_virus():
    h = discord.Embed(title = "Virus Command", color = 0x6691D9, description = "Inject a virus into someone")
    h.add_field(name = "Usage", value = "`?virus <@user>`")
    h.add_field(name = "Note", value = "Don't overuse this")
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
    h.add_field(name = "Note", value = "Disabled (WIP)")
    await bot.say(embed = h)

@bot.command()
async def help_ban():
    h = discord.Embed(title = "Ban Command", color = 0x6691D9, description = "Bans the given user")
    h.add_field(name = "Usage", value = "`?ban <@user> or <username>`")
    h.add_field(name = "Note", value = "Disabled (WIP)")
    await bot.say(embed = h)

@bot.command()
async def help_warn():
    h = discord.Embed(title = "Say Command", color = 0x6691D9, description = "Warns the given user with a reason")
    h.add_field(name = "Usage", value = "`?warn <@user> <reason>`")
    h.add_field(name = "Note", value = "Disabled (WIP)")
    await bot.say(embed = h)

@bot.command()
async def help_mute():
    h = discord.Embed(title = "Mute Command", color = 0x6691D9, description = "Mutes the given user for any amount of time")
    h.add_field(name = "Usage", value = "`?mute <@user> or <username> <time>`")
    h.add_field(name = "Note", value = "Empty...")
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
    
bot.loop.create_task(my_background_task())
if not os.environ.get('TOKEN'):
    print("no token found!")
bot.run(os.environ.get('TOKEN').strip('"'))
