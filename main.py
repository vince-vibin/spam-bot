from dotenv import load_dotenv

from discord_slash import SlashCommand
from discord_slash import SlashContext

import discord
from discord.ext.commands import Bot

import os
import time

intents = discord.Intents.default()
intents.members = True

bot = Bot(command_prefix="+", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

load_dotenv()
TOKEN = os.getenv("TOKEN")

# video: https://youtu.be/CE0noW3flT8

@bot.event
async def on_ready():
    activity = discord.Game(name="finn abfucken")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("ready um Finn abzufucken")

    @slash.slash(name="abfuck", description="hello!")
    async def abfuck(self, ctx: SlashContext):
        await member.send("hello")

    @bot.command()
    async def abfuck(ctx, member: discord.Member, msg):
        i=0
        while True:
            i=i+1
            await member.send(msg + "\ncount: " + str(i))
            print("send message to " + str(member) + " \nmessage: " + msg + "\n count: " + str(i) + "\n------------------")
            time.sleep(3)

bot.run(TOKEN)