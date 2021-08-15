import discord, os, json
from discord.ext import commands
from core.class_setting import Cog_Extension


with open("read_info.json", "r", encoding="utf8") as j_file:
    j_data = json.load(j_file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">>", help_command=None, intents=intents)

@bot.event
async def on_ready():
    print(">>System:Bot is online.")

@bot.event
async def on_member_join(member):
    # print(f"{member} join!" )
    channel = bot.get_channel(855062319050260514)
    await channel.send(f">>{member} join!")
    await channel.send(">>Hi")
    await channel.send(">>Nice to see you!")
@bot.event
async def on_member_remove(member):
    # print(f"{member} remove!" )
    channel = bot.get_channel(855062319050260514)
    await channel.send(f"{member} leaved just now O.o")

# @bot.command()
# async def load(ctx, extension):
#     bot.load_extension("cmds.%s" %extension)
#     await ctx.send(">>Load %s successfully." %extension)
# @bot.command()
# async def unload(ctx, extension):
#     bot.unload_extension("cmds.%s" %extension)
#     await ctx.send(">>Unload %s successfully." %extension)

def authentication(id):
    return True if id == 776807118481129532 else False

@bot.command()
async def dev(ctx):
    if authentication(ctx.author.id) == True:
        embed=discord.Embed(title="==Developer_Commands==", color=0xf6a7cb)
        embed.add_field(name=">>dev_reload [name]", value="Reload File.", inline=False)
        embed.add_field(name=">>dev_cls [amounts]", value="Clean messages.", inline=False)
        embed.add_field(name=">>dev_announce [messages]", value="Announce messages.", inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Sorry! You DO NOT have the permission.")

@bot.command()
async def dev_reload(ctx, extension):
    if authentication(ctx.author.id) == True:
        bot.reload_extension(f"cmds.{extension}")
        await ctx.send(f">>Developer: Reload {extension} successfully.")
    else: 
        await ctx.send("Sorry! You DO NOT have the permission.")
@bot.command()
async def dev_cls(ctx, amount):
    if authentication(ctx.author.id) == True:
        await ctx.channel.purge(limit=int(amount)+1)
    else:
        await ctx.send("Sorry! You DO NOT have the permission.")
@bot.command()
async def dev_announce(ctx, *, msg):
    if authentication(ctx.author.id) == True:
        await ctx.message.delete()
        await ctx.send(f"```FrontierBot Update:\n{msg}```")
    else: 
        await ctx.send("Sorry! You DO NOT have the permission.")

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

##### THIS IS VERY IMPORTANT ##### 
# Run the main file : bot.py
if __name__ == "__main__":
    bot.run(j_data["token"])
##### THIS IS VERY IMPORTANT #####