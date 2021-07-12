import discord, json, asyncio
from datetime import datetime, timezone, timedelta
from discord.ext import commands, tasks
from core.class_setting import Cog_Extension


class task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        async def status():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(">>help"))
                await asyncio.sleep(120)
        self.backgroundTa = self.bot.loop.create_task(status())
        async def hello():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(855062319435087872)
            while not self.bot.is_closed():
                if datetime.now(timezone(timedelta(hours=+8))).strftime("%H%M%S") == "073000":
                    await self.channel.send("Goodmorning! 早安! おはようございます!")
                    await asyncio.sleep(1)
                elif datetime.now(timezone(timedelta(hours=+8))).strftime("%H%M%S") == "223000":
                    await self.channel.send("Goodnight! 晚安! おやすみなさい!")
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.backgroundTb = self.bot.loop.create_task(hello())

    @commands.command()
    async def setChannel(self, ctx, channel):
        if ctx.channel == self.channel and ctx.author.id == 776807118481129532:
            self.channel = self.bot.get_channel(int(channel))


def setup(bot):
    bot.add_cog(task(bot))