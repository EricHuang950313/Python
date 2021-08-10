import discord, os, json
from discord.ext import commands
from core.class_setting import Cog_Extension


with open("setting.json", "r", encoding="utf8") as j_file:
    j_data = json.load(j_file)

class picture(Cog_Extension):
    @commands.command()
    async def ty(self, ctx):
        picture = j_data["ty"]
        await ctx.send(picture)
    @commands.command()
    async def winnie(self, ctx):
        picture = j_data["winnie"]
        await ctx.send(picture)


def setup(bot):
    bot.add_cog(picture(bot))