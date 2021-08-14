import discord
from discord.ext import commands
from core.class_setting import Cog_Extension


class helpcommand(Cog_Extension):  
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed=discord.Embed(title=">> H E L P    C O M M A N D S", description="Type \">>help\" command for more information about FrontierGuard. <Ver1.0>", color=0xf6a7cb)
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2020/10/31/19/25/robot-5702074_1280.png")
        embed.add_field(name="Ⅰ.ANNOUNCEMENT", value=">>help tba", inline=False)
        embed.add_field(name="Ⅱ.ECONOMY", value=">>help eco", inline=False)
        embed.add_field(name="Ⅲ.PICTURE", value=">>help pic", inline=False)
        embed.add_field(name="Ⅳ.ENCYCLOPEDIA", value=">>help ency", inline=False)
        embed.add_field(name="<S>.errorCODE", value=">>help eC", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def tba(self, ctx):
        embed=discord.Embed(title="==ANNOUNCEMENT==", color=0xf6a7cb)
        embed.add_field(name=">>F [member]", value="FingBot will say this to someone if you think someone's action is fu*king idiot.", inline=False)
        embed.add_field(name=">>saysub [user_input]", value="FingBot will say this if you don't want the other know the author.", inline=False)
        await ctx.send(embed=embed)
    @help.command()
    async def eco(self, ctx):
        embed=discord.Embed(title="==ECONOMY==", color=0xf6a7cb)
        embed.add_field(name=">>register", value="Register an account.", inline=False)
        await ctx.send(embed=embed)
    @help.command()
    async def pic(self, ctx):
        embed=discord.Embed(title="==PICTURE==", color=0xf6a7cb)
        embed.add_field(name=">>ty", value="Aka emoji\":heart:\"or\":heart_eyes:\".", inline=False)
        embed.add_field(name=">>winnie", value="Winnie^^", inline=False)
        await ctx.send(embed=embed)
    @help.command()
    async def ency(self, ctx):
        embed=discord.Embed(title="==ENCYCLOPEDIA==", color=0xf6a7cb)
        embed.add_field(name=">>gayboi", value="The contents of who is gayboy.", inline=False)
        await ctx.send(embed=embed)
    @help.command()
    async def eC(self, ctx):
        embed=discord.Embed(title="==errorCODE==", color=0xf6a7cb)
        embed.add_field(name="errorCODE=001", value="Out of time error.", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(helpcommand(bot))