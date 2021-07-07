import discord, os, json, asyncio
from discord.ext import commands
from core.class_setting import Cog_Extension
from discord import User


with open("setting.json", "r", encoding="utf8") as j_file:
    j_data = json.load(j_file)

class text(Cog_Extension):              
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed=discord.Embed(title="Terminal H E L P Commands", description="Terminal commands.", color=0x000f5c)
        embed.add_field(name="Ⅰ. GET ROLE", value="1. Add a reaction\n💻 : PROGRAMMER ONLY / 🎮 : PROGAMER ONLY\n2. Type \"--ter getrole\" to get role", inline=True)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def getrole(self, ctx):
        if Cog_Extension._statusaa == True:
            await Cog_Extension._aa[0].add_roles(Cog_Extension._aa[1].get_role(861559887078359040)) #role's id 
            Cog_Extension._aa = []
            Cog_Extension._statusaa == False
        elif Cog_Extension._statusbb == True:
            await og_Extension._bb[0].add_roles(og_Extension._bb[1].get_role(861559967114854411)) #role's id
            Cog_Extension._bb = []
            Cog_Extension._statusbb == False
        else:
            ctx.send("Terminal: No role to get.")
   
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        if str(data.emoji) == "💻" and data.message_id==861816265790062623: #message's id
            guild = self.bot.get_guild(data.guild_id)
            Cog_Extension._aa.append(data.member) 
            Cog_Extension._aa.append(guild) 
            Cog_Extension._statusaa = True
        if str(data.emoji) == "🎮" and data.message_id==861816265790062623: #message's id
            guild = self.bot.get_guild(data.guild_id)
            Cog_Extension._bb.append(data.member) 
            Cog_Extension._bb.append(guild) 
            Cog_Extension._statusbb = True
        
def setup(bot):
    bot.add_cog(text(bot))