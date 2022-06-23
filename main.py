from dotenv import load_dotenv
import json
import os
import time

import discord
from discord.ext.commands import Bot

import random

intents = discord.Intents.default()
intents.members = True

bot = Bot(command_prefix="+", intents=discord.Intents.all())

load_dotenv()
TOKEN = os.getenv("TOKEN")

whitelist = open("users.json")
whitelist = json.load(whitelist)

@bot.event
async def on_ready():
    activity = discord.Game(name="spamming")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("ready to spam")

def checkMember(member):
    for i in whitelist["ultra"]:
        if i == member:
            return "ultra"
        else:
            for i in whitelist["thorns"]:
                if i == member:
                    return "thorns"
            else:   
                return "error"

def checkAuthor(author):
    return false

@bot.command()
async def abfuck(ctx, member: discord.Member, msg):
    print(ctx.author)
    memberStr = str(member)
    if checkMember(memberStr) == "ultra":
        await ctx.send(memberStr + " has ultra rank")
    elif checkMember(memberStr) == "thorns":
        await ctx.send("Jokes on you " + memberStr + " has thorns prepare for the worst")

bot.run(TOKEN)