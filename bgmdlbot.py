import discord
from random import *
import config
import datetime
import time
from discord.ext.commands import Bot
from discord.ext import commands
Client = discord.Client
bot_prefix="`"
client = commands.Bot(command_prefix=bot_prefix)
status = "being cool lol"


@client.event
async def on_ready():
    print("Bot online!")
    print("Name= {}".format(client.user.name))
    print("ID= {}".format(client.user.id))


@client.command()
async def say(ctx):
    d = randint(1,10)
    if d == 5:
        await client.say("no ur dumb and so is @astrosguy :dab:")
    else:
        um,ah,bh = ctx.partition(' ')
        await client.say(bh)



@client.event
async def on_message(message):
    if message.channel.is_private:
            if "offers" in message.content.lower() or "offer" in message.content.lower():
                if not message.author.id == client.user.id:
                    f = open("freeagency.txt", "a+")
                    timey = message.timestamp
                    timey.strftime('%m / %d , %I %p : %M : %S')
                    timey = str(timey)
                    name = message.author.name
                    name = str(name)
                    name = name.encode('utf-8')
                    name = str(name)
                    name = name.strip("'")
                    name = name[2:]
                    f.write(name)
                    f.write(":\t")
                    f.write(message.content)
                    f.write("\t")
                    f.write(timey)
                    f.write("\n")
                    f.close()
                    await client.send_message(message.channel, 'Offer has been recorded.')
            elif "pitch" in message.content.lower():
                if not message.author.id == client.user.id:
                    f = open("freeagencypitch.txt", "a+")
                    timey = message.timestamp
                    timey.strftime('%m / %d , %I %p : %M : %S')
                    timey = str(timey)
                    name = message.author.name
                    name = str(name)
                    name = name.encode('utf-8')
                    name = str(name)
                    name = name.strip("'")
                    name = name[2:]
                    f.write(message.author.name)
                    f.write("\t")
                    f.write(message.content)
                    f.write("\t")
                    f.write(timey)
                    f.write("\n")
                    f.close()
                    await client.send_message(message.channel, 'Pitch has been recorded.')
            else:
                if not message.author.id == client.user.id:
                    await client.send_message(message.channel, "Please submit a free agency offer using"                                             
                                                               " the format: Team offers x through y")
                    await client.send_message(message.channel, "Where x is money, and y is years")
                    await client.send_message(message.channel, "If you wish to submit a pitch,"
                                                           "please type the word Pitch before your pitch")

    await client.process_commands(message)


@client.command()
async def ping():
    await client.say("Pong!")


@client.command(pass_context=True)
async def free_agent():
    f = open("freeagency.txt","a+")
    for i in range(2):
        f.write("hello\n")


client.run(config.api_key)