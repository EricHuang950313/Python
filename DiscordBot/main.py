import discord
from discord.ext import commands
import json

with open("setting.json", "r", encoding="utf8") as j_file:
    j_data = json.load(j_file)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">>", intents=intents)

@bot.event
async def on_ready():
    print(">> Bot is online")

@bot.event
async def on_member_join(member):
    # print("%s join!" %(member))
    channel = bot.get_channel(846674619108556823)
    await channel.send(">>"+str(member)+" join!")
    await channel.send(">>Hi")
    await channel.send(">>Nice to see you!")

@bot.event
async def on_member_remove(member):
    # print("%s remove!" %(member))
    channel = bot.get_channel(846674619108556823)
    await channel.send(">>"+str(member)+" leave!")

@bot.command()
async def Gayboi(ctx):
    await ctx.send("Fing_Bot百科")
    await ctx.send("張董，又稱GAYBOI，又稱GAY炮部長，又稱苗栗國財政部長")
    await ctx.send("喜歡睡覺，不喜歡設鬧鐘")

@bot.command()
async def ty(ctx):
    picture = j_data["ty"]
    await ctx.send(picture)

if __name__ == "__main__":
	bot.run(j_data["token"])