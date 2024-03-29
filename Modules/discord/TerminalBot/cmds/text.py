import discord, os, json, asyncio
from discord.ext import commands
from core.class_setting import Cog_Extension
from discord import User


with open("setting.json", "r", encoding="utf8") as j_file:
    j_data = json.load(j_file)

class text(Cog_Extension):   
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        if str(ctx.channel) == "🖥terminal":
            embed=discord.Embed(title="Terminal H E L P Commands", description="Terminal commands.", color=0x000f5c)
            embed.add_field(name="Ⅰ. GET ROLE", value="1. Add a reaction\n💻 : PROGRAMMER ONLY / 🎮 : PROGAMER ONLY\n2. Type \"--ter getrole\" to get role", inline=True)
            embed.add_field(name="Ⅰ. REMOVE ROLE", value="1. Add a reaction\n💻 : PROGRAMMER ONLY / 🎮 : PROGAMER ONLY", inline=True)
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed, delete_after=60.0)
        else:
          pass
    @commands.command()
    async def getrole(self, ctx):
        if str(ctx.channel) == "🖥terminal":
          await ctx.channel.purge(limit=1)  
          if Cog_Extension._statusaa == Cog_Extension._statusbb == False:
            await ctx.send("Terminal: No role to get.", delete_after=10.0)
          if Cog_Extension._statusaa == True:
            await Cog_Extension._aa[0].add_roles(Cog_Extension._aa[1].get_role(862222470111166465)) #role's id 
            await Cog_Extension._aa[0].send("You get role: \"Programmer\"")
            Cog_Extension._aa = []
            Cog_Extension._statusaa = False
          if Cog_Extension._statusbb == True:
            await Cog_Extension._bb[0].add_roles(Cog_Extension._bb[1].get_role(856450756789927937)) #role's id
            await Cog_Extension._bb[0].send("You get role: \"Progamer\"")
            Cog_Extension._bb = []
            Cog_Extension._statusbb = False
        else:
          pass
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        if str(data.emoji) == "💻" and data.message_id==863316445378117642: #message's id
            guild = self.bot.get_guild(data.guild_id)
            Cog_Extension._aa.append(data.member) 
            Cog_Extension._aa.append(guild) 
            Cog_Extension._statusaa = True
        if str(data.emoji) == "🎮" and data.message_id==863316445378117642: #message's id
            guild = self.bot.get_guild(data.guild_id)
            Cog_Extension._bb.append(data.member) 
            Cog_Extension._bb.append(guild) 
            Cog_Extension._statusbb = True
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        if str(data.emoji) == "💻" and data.message_id==863316445378117642: #message's id
            guild = self.bot.get_guild(data.guild_id)
            user = guild.get_member(data.user_id)
            role = guild.get_role(862222470111166465) #role's id
            await user.remove_roles(role)
            await user.send("You removed role: \"Programmer\"")
        if str(data.emoji) == "🎮" and data.message_id==863316445378117642: #message's id
            guild = self.bot.get_guild(data.guild_id)
            user = guild.get_member(data.user_id)
            role = guild.get_role(856450756789927937) #role's id
            await user.remove_roles(role)
            await user.send("You removed role: \"Progamer\"")
        
def setup(bot):
    bot.add_cog(text(bot))