import discord
from discord.ext import commands
from core.class_setting import Cog_Extension


class helpcommand(Cog_Extension):
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        if ctx.message.content[5:] not in ["tba", "eco", "ency", "pic", "eC", "help"]:
            await ctx.send("Command NOT FOUND! (errorCODE=001)")
            await ctx.send("Try\">>help\" for checking commands.")
        else:
            embed=discord.Embed(title="ＵＳＥＲ  ＧＵＩＤＥ", description="\">>help\" command helps you easily get hang of using the bot.", color=0xffca57)
            embed.add_field(name="VERSION", value="<Ver1.9.0Beta>", inline=False)
            embed.add_field(name="Ⅰ. ANNOUNCEMENT", value=">>help tba", inline=False)
            embed.add_field(name="Ⅱ. ECONOMY", value=">>help eco", inline=False)
            embed.add_field(name="Ⅲ. ENCYCLOPEDIA", value=">>help ency", inline=False)
            embed.add_field(name="Ⅳ. PICTURE", value=">>help pic", inline=False)
            embed.add_field(name="<S>. errorCODE", value=">>help eC", inline=False)
            await ctx.send(embed=embed)

    @help.command()
    async def tba(self, ctx):
        embed=discord.Embed(title="ANNOUCEMENT", color=0xffca57)
        embed.add_field(name=">>F [member]", value="Bot will say something to [member] if you think [member]'s action is idiot.", inline=False)
        embed.add_field(name=">>saysub [user_input]", value="Bot will say [user_input] instead of you.", inline=False)
        await ctx.send(embed=embed)
    @help.command()
    async def eco(self, ctx):
        embed=discord.Embed(title="ECONOMY", color=0xffca57)
        embed.add_field(name=">>register", value="Register an account.", inline=False)
        embed.add_field(name=">>deposit", value="Check your account's deposit.", inline=False)
        embed.add_field(name=">>to", value="Transfer $ between bank and wallet.", inline=False)
        embed.add_field(name=">>work", value="Work for 60~90mins to earn 150~250$.", inline=False)
        embed.add_field(name=">>give [member] [$amount]", value="Give [member] [$amount]$.", inline=False)
        embed.add_field(name=">>rob [bank/member]", value="Rob some money from bank or member.", inline=False)
        await ctx.send(embed=embed)
    @help.command()
    async def ency(self, ctx):
        embed=discord.Embed(title="ENCYCLOPEDIA", color=0xffca57)
        embed.add_field(name=">>gayboi", value="Encyclopedia of gayboy.", inline=False)
        await ctx.send(embed=embed)
    @help.command()
    async def pic(self, ctx):
        embed=discord.Embed(title="PICTURE", color=0xffca57)
        embed.add_field(name=">>ty", value="As known as emoji \":heart:\" or \":heart_eyes:\".", inline=False)
        embed.add_field(name=">>winnie", value="CN Winnie.", inline=False)
        await ctx.send(embed=embed)
    @help.command()
    async def eC(self, ctx):
        embedA=discord.Embed(color=0xffca57)
        embedB=discord.Embed(color=0xffca57)
        embedC=discord.Embed(color=0xffca57)
        embedA.add_field(name="errorCODE starts with 0 (Command input error):", value="\u200b", inline=False)
        embedA.add_field(name="errorCODE=001", value="Command not found error.", inline=False)
        embedA.add_field(name="errorCODE=002", value="Exception error.", inline=False)
        embedB.add_field(name="errorCODE starts with 1 (Economy user input error):", value="\u200b", inline=False)
        embedB.add_field(name="errorCODE=101", value="Out of time error.", inline=False)
        embedB.add_field(name="errorCODE=102", value="Value incorrect error.\n", inline=False)
        embedC.add_field(name="errorCODE starts with 2 (Background tasks system error):", value="\u200b", inline=False)
        embedC.add_field(name="errorCODE=201", value="FOR GOODMORNING/GOODNIGHT: Same ranking if deviation in 1.5 second.\n", inline=False)
        await ctx.send(embed=embedA)
        await ctx.send(embed=embedB)
        await ctx.send(embed=embedC)

def setup(bot):
    bot.add_cog(helpcommand(bot))