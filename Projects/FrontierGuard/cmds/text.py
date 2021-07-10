import discord, os, json, asyncio
from discord.ext import commands
from core.class_setting import Cog_Extension
from discord import User


with open("setting.json", "r", encoding="utf8") as j_file:
    j_data = json.load(j_file)

class text(Cog_Extension):      
    @commands.command()
    async def gayboi(self, ctx):
        for i in range(5):
            await asyncio.sleep(1)
            await ctx.send(j_data["Gayboi_"+str(i+1)]) 
    @commands.command()
    async def F(self, ctx, user_name):
        guild = self.bot.get_guild(846674619108556820)
        for member in guild.members:
            if user_name == str(member)[:-5]:
                await ctx.send(member.mention+j_data["F"])  
            else:
                pass
        
        
def setup(bot):
    bot.add_cog(text(bot))