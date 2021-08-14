import discord, os, json, asyncio
from discord.ext import commands
from discord import User
from core.class_setting import Cog_Extension


with open("read_info.json", "r", encoding="utf8") as j_file:
    j_data = json.load(j_file)

class text(Cog_Extension):
    @commands.command()
    async def F(self, ctx, user_name):
        guild = self.bot.get_guild(855062319036760104)
        for member in guild.members:
            if user_name == str(member)[:-5]:
                await ctx.send(member.mention+j_data["F"])  
            else:
                pass
    @commands.command()
    async def saysub(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(f"Somebody wants to say: {str(msg)}")
    @commands.command()
    async def gayboi(self, ctx):
        for i in range(5):
            await asyncio.sleep(1)
            await ctx.send(j_data[f"Gayboi_{str(i+1)}"])
        
        
def setup(bot):
    bot.add_cog(text(bot))