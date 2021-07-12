import discord, os, json, asyncio
from discord.ext import commands
from core.class_setting import Cog_Extension


class economy(Cog_Extension):
    @commands.command()
    async def register(self, ctx):
        def check_A(msgg):
            global pasA
            if msgg.content=="A" and msgg.channel==ctx.channel and msgg.author==ctx.author:
              pasA = True
              return True
            elif msgg.content=="B" and msgg.channel==ctx.channel and msgg.author==ctx.author:
              pasA = False
              return True
        def check_B(msgg):
            global pasB
            pasB = True
            with open("./economyData/eco_account.json", mode="r", encoding="utf-8") as file:
                data = json.load(file)
                for i in data:
                    if msgg.content==data[i] and msgg.channel==ctx.channel and msgg.author==ctx.author or str(msgg.author.id)==str(i) and msgg.channel==ctx.channel and msgg.author==ctx.author:
                        pasB = False
                        return True
            if pasB == True:
              with open("./economyData/eco_account.json", mode="w", encoding="utf-8") as file:
                  data[str(ctx.author.id)] = str(msgg.content)
                  json.dump(data, file, indent=4)
              return True

        await ctx.send("Please enter: \"A\" to start the process. \"B\" to leave.")
        try:
            await self.bot.wait_for(event="message",check=check_A, timeout=15)
        except asyncio.TimeoutError:
            await ctx.send("Register failed!")
        else:
            if pasA == True:
                await ctx.send("Please enter your user name(Name can not be changed!).")
                try:
                    await self.bot.wait_for(event="message",check=check_B, timeout=60)
                except asyncio.TimeoutError:
                    await ctx.send("Register failed!")
                else:
                    if pasB == True:
                        await ctx.send("Register successfily.")
                    elif pasB == False:
                        await ctx.send("You have already registered an Account.")
            elif pasA == False:
                await ctx.send("Already leaved.")
    @commands.command()
    async def allaccountdata(self, ctx):
        with open("./economyData/eco_account.json", mode="r", encoding="utf-8") as file:
                data = json.load(file)
                for i in data:
                    if i == "Test_S":
                        continue
                    else:
                        await ctx.send("==BANK Accounts==```"+data[i]+"```")

def setup(bot):
    bot.add_cog(economy(bot))