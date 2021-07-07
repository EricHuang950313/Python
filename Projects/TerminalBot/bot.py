import discord, os, json
from discord.ext import commands
from core.class_setting import Cog_Extension
import keep_alive


with open("setting.json", "r", encoding="utf8") as j_file:
    j_data = json.load(j_file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="--ter ", intents=intents, help_command=None)

@bot.event 
async def on_ready():
    print("Terminal Status: Online.")
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(861535788499992586)
    await channel.send("@everyone Terminal Update: `"+str(member)+"` joined the server!")
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(861535788499992586)
    await channel.send("@everyone Terminal Update: `"+str(member)+"` leaved the server!")    

# @bot.command()
# async def load(ctx, extension):
#     bot.load_extension("cmds.%s" %extension)
#     await ctx.send("Terminal developer update: Load %s successfully." %extension)
# @bot.command()
# async def unload(ctx, extension):
#     bot.unload_extension("cmds.%s" %extension)
#     await ctx.send("Terminal developer update: Unload %s successfully." %extension)

@bot.command()
async def reload(ctx, extension):
    if str(ctx.channel) == "指令區":
      bot.reload_extension("cmds.%s" %extension)
      await ctx.send("Terminal Developer Update: Reload %s successfully." %extension)
    else:
      pass

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension("cmds.%s" %filename[:-3])

if __name__ == "__main__":
    bot.run(j_data["token"])