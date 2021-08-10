import discord, os, json
from discord.ext import commands
from core.class_setting import Cog_Extension
import keep_alive


with open("setting.json", "r", encoding="utf8") as j_file:
    j_data = json.load(j_file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">>", help_command=None, intents=intents)
client = discord.Client()

@bot.event
async def on_ready():
    print(">>System:Bot is online.")

@bot.event
async def on_member_join(member):
    # print("%s join!" %(member))
    channel = bot.get_channel(855062319050260514)
    await channel.send(">>"+str(member)+" join!")
    await channel.send(">>Hi")
    await channel.send(">>Nice to see you!")

@bot.event
async def on_member_remove(member):
    # print("%s remove!" %(member))
    channel = bot.get_channel(855062319050260514)
    await channel.send(">>"+str(member)+" leave!")

# @bot.command()
# async def load(ctx, extension):
#     bot.load_extension("cmds.%s" %extension)
#     await ctx.send(">>Load %s successfully." %extension)

# @bot.command()
# async def unload(ctx, extension):
#     bot.unload_extension("cmds.%s" %extension)
#     await ctx.send(">>Unload %s successfully." %extension)

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 776807118481129532:
        bot.reload_extension("cmds.%s" %extension)
        await ctx.send(">>Developer: Reload %s successfully." %extension)
    else: 
        pass
@bot.command()
async def cls(ctx, amount):
    if ctx.author.id == 776807118481129532:
      await ctx.channel.purge(limit=int(amount)+1)
    else:
      pass
@bot.command()
async def saydev(ctx, *, msg):
    if ctx.author.id == 776807118481129532:
        await ctx.message.delete()
        await ctx.send(str(msg))
    else: 
        pass

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension("cmds.%s" %filename[:-3])

##### THIS IS VERY IMPORTANT ##### 
# Run the main file : bot.py
if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(j_data["token"])
##### THIS IS VERY IMPORTANT #####