from dotenv import load_dotenv
import json
import os
import time

import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix="-", intents=discord.Intents.all())

load_dotenv()
TOKEN = os.getenv("TOKEN")

whitelist = open("users.json")
whitelist = json.load(whitelist)

premiumLimit = 50
standardLimit = 20
ultraLimit = 100

@bot.event
async def on_ready():
    activity = discord.Game(name="spamming / Prefix: -")
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
    for i in whitelist["spammerPremium"]:
        if i == author:
            return "premium"
        else:
            for i in whitelist["ultra"]:
                if i == author:
                    return "ultra"
                else:
                    return "standard"

async def spamming(victim, limit, msg):
    i = 0
    msg = " ".join(str(x) for x in msg)
    while limit > i:
        i=i+1
        embed = discord.Embed(colour=0xFF1828)
        embed.add_field(name=msg, value="jokes on you", inline=False)
        await victim.send(embed=embed)
        time.sleep(1)

@bot.command()
async def spam(ctx, member: discord.Member, *msg):
    memberStr = str(member)[:-5]

    authorStr = str(ctx.author)[:-5]

    memberState = checkMember(memberStr)
    authorState = checkAuthor(authorStr)

    if memberState == "ultra":
        embed = discord.Embed(colour=0xFF1828)
        embed.add_field(name=memberStr + " has ultra rank", value="how dare you try to challenge the ultra ranked", inline=False)
        embed.set_footer(text="prepair for the worst")
        await ctx.send(embed=embed)

        embed = discord.Embed(colour=0x4AFB71)
        embed.add_field(name=authorStr + " has tried to spam you", value="but was denied", inline=False)
        await member.send(embed=embed)

        await spamming(ctx.author, 100, "how dare you try to challenge the ultra ranked")

    elif memberState == "thorns":
        embed = discord.Embed(colour=0xFF1828)
        embed.add_field(name=memberStr + " has thorns", value="Jokes on you", inline=False)
        embed.set_footer(text="prepair for the worst")
        await ctx.send(embed=embed)

        embed = discord.Embed(colour=0x4AFB71)
        embed.add_field(name=authorStr + " has tried to spam you", value="but was denied", inline=False)
        await member.send(embed=embed)

        await spamming(ctx.author, standardLimit, memberStr + " has thorns so jokes on you")

    elif authorState == "premium":
        embed = discord.Embed(colour=0x4AFB71)
        embed.add_field(name="spamming " + memberStr, value="have fun", inline=False)
        embed.set_footer(text="author rank: " + authorState + "\nspamlimit: " + str(premiumLimit))
        await ctx.send(embed=embed)

        await spamming(member, premiumLimit, msg)

    elif authorState == "ultra":
        embed = discord.Embed(colour=0x4AFB71)
        embed.add_field(name="spamming " + memberStr, value="have fun", inline=False)
        embed.set_footer(text="author rank: " + authorState + "\nspamlimit: " + str(ultraLimit))
        await ctx.send(embed=embed)

        await spamming(member, premiumLimit, msg)
    else:
        embed = discord.Embed(colour=0x4AFB71)
        embed.add_field(name="spamming " + memberStr, value="have fun", inline=False)
        embed.set_footer(text="author rank: " + authorState + "\nspamlimit: " + str(standardLimit))
        await ctx.send(embed=embed)

        await spamming(member, standardLimit, msg)

bot.run(TOKEN)

#vince_vibin#7429