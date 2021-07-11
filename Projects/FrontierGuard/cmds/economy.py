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
          with open("eco_account.txt", mode="r", encoding="utf-8") as user_file:
            for i in user_file:
                if msgg.content==str(i) and msgg.channel==ctx.channel and msgg.author==ctx.author:
                    pasB = False
                    return True
          if pasB == True:
            with open("eco_account.txt", mode="a", encoding="utf-8") as user_file:
              user_file.write(msgg.content)
            return True
          

        await ctx.send("Please enter: \"A\" to start the process./\"B\" to leave.")
        try:
          await self.bot.wait_for(event="message",check=check_A, timeout=15)
        except asyncio.TimeoutError:
          await ctx.send("Register failed!")
        else:
          if pasA == True:
            await ctx.send("Please enter your user name.")
            try:
              await self.bot.wait_for(event="message",check=check_B, timeout=60)
            except asyncio.TimeoutError:
              await ctx.send("Register failed!")
            else:
              if pasB == False:
                await ctx.send("Account already existed.")
              elif pasB == True:
                await ctx.send("Register successfily.")
          elif pasA == False:
            await ctx.send("Already leaved.")


def setup(bot):
    bot.add_cog(economy(bot))