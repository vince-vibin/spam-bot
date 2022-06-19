from dotenv import load_dotenv
import json

from discord_slash import SlashCommand
from discord_slash import SlashContext

import discord
from discord.ext.commands import Bot

import os

intents = discord.Intents.default()
intents.members = True

bot = Bot(command_prefix="+", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

load_dotenv()
TOKEN = os.getenv("TOKEN")

# video: https://youtu.be/CE0noW3flT8

whitelist = open("whitelist.json")
whitelist = json.load(whitelist)

@bot.event
async def on_ready():
    activity = discord.Game(name="finn abfucken")
    await bot.change_presence(status=discord.Status.online, activity=activity)

    

    print("ready um Finn abzufucken")

def checkMember(member):
    for i in whitelist["ultra"]:
        if i == member:
            return "ultra"
        else:
            for i in whitelist["protectionPremium"]:
                return "premium"
            else:
                for i in whitelist["protectionLow"]:
                    return "low"
                else:
                    return False

    
@bot.command()
async def abfuck(ctx, member: discord.Member, msg):
    member = str(member)
    if checkMember(member) == "ultra":
        await ctx.send(member + " has ultra rank")
    else: 
        i=0
        while True:
            i=i+1
            await member.send(msg + "\ncount: " + str(i))
            print("send message to " + member + " \nmessage: " + msg + "\n count: " + str(i) + "\n------------------")
            time.sleep(3)

bot.run(TOKEN)