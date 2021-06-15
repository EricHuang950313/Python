import discord, os, json, asyncio
from discord.ext import commands
from core.class_setting import Cog_Extension
from discord import User


with open("setting.json", "r", encoding="utf8") as j_file:
    j_data = json.load(j_file)

class Text(Cog_Extension):      
    # Group:help(General Introduction) ---Start--- 
    ###
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed=discord.Embed(title=">> H E L P    C O M M A N D S", description="Type \">>help\" command for more information about Fing_Bot commands.", color=0xf6a7cb)
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2020/10/31/19/25/robot-5702074_1280.png")
        embed.add_field(name="Ⅰ.ENCYCLOPEDIA", value=">>help ency", inline=True)
        embed.add_field(name="Ⅱ.PICTURE", value=">>help pic", inline=True)
        embed.add_field(name="Ⅲ.ANNOUNCEMENT", value=">>help tba", inline=False)
        await ctx.send(embed=embed)
    ###    
    # Group:help(General Introduction) ---End ---
    # Subcommand:>>help (option) ---Start
    # a.ency_1
    @help.command()
    async def ency(self, ctx):
        embed=discord.Embed(title="==ENCYCLOPEDIA==", color=0xf6a7cb)
        embed.add_field(name=">>gayboi", value="The contents of who is gayboy.", inline=False)
        await ctx.send(embed=embed)
    # b.pic_1
    @help.command()
    async def pic(self, ctx):
        embed=discord.Embed(title="==PICTURE==", color=0xf6a7cb)
        embed.add_field(name=">>ty", value="Aka emoji\":heart:\"or\":heart_eyes:\".", inline=False)
        await ctx.send(embed=embed)
    # c.ency_1
    @help.command()
    async def tba(self, ctx):
        embed=discord.Embed(title="==ANNOUNCEMENT==", color=0xf6a7cb)
        embed.add_field(name=">>meet", value="An announcement for announcing a meeting.", inline=False)
        embed.add_field(name=">>F [member]", value="FingBot will say this to someone if you think someone's action is fu*king idiot.", inline=False)
        await ctx.send(embed=embed)
    # Subcommand:>>help (option) ---End
   
        
    @commands.command()
    async def gayboi(self, ctx):
        for i in range(5):
            await asyncio.sleep(1)
            await ctx.send(j_data["Gayboi_"+str(i+1)])
    @commands.command()
    async def meet(self, ctx):
        await ctx.send(j_data["meet"])   


    @commands.command()
    async def F(self, ctx, user_name):
        guild = self.bot.get_guild(846674619108556820)
        for member in guild.members:
            if user_name == str(member)[:-5]:
                await ctx.send(member.mention+j_data["F"])  
            else:
                pass
        
def setup(bot):
    bot.add_cog(Text(bot))