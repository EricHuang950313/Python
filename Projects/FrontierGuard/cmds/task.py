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
        
        async def checklist():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(855062319435087872)
            while not self.bot.is_closed():
                if datetime.now(timezone(timedelta(hours=+8))).strftime("%H%M%S") == "075900" or datetime.now(timezone(timedelta(hours=+8))).strftime("%H%M%S") == "225900":
                    with open("check.json", "r", encoding="utf-8") as checkrl_file:
                        try:
                            checkl_data = json.load(checkrl_file)
                            op = ""
                            for i in checkl_data:
                                op = op + i + "\n"
                            await self.channel.send("Sign In Result aka 點名結果::\n```"+op+"```")
                            clear = True
                        except json.decoder.JSONDecodeError:
                            await self.channel.send("Sign In Result aka 點名結果: ```None! 沒人```")
                            clear = False
                    if clear == True:
                        with open("check.json", "w", encoding="utf-8") as checkwl_file:
                            clear = False
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.backgroundTc = self.bot.loop.create_task(checklist())

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "早安" and (int(datetime.now(timezone(timedelta(hours=+8))).strftime("%H%M")) - 730) >= 0 and (int(datetime.now(timezone(timedelta(hours=+8))).strftime("%H%M")) - 730) < 30:
            with open("check.json", "r", encoding="utf-8") as checkr_file:
                try:
                    check_data = json.load(checkr_file)
                    first = False
                except json.decoder.JSONDecodeError:
                    first = True
            with open("check.json", "w", encoding="utf-8") as checkw_file:
                if first == True:
                    json.dump({str(msg.author):"True"}, checkw_file, indent=4)
                    first = False
                else:
                    check_data[str(msg.author)] = "True"
                    json.dump(check_data, checkw_file, indent=4)
        if msg.content == "晚安" and (int(datetime.now(timezone(timedelta(hours=+8))).strftime("%H%M")) - 2230) >= 0 and (int(datetime.now(timezone(timedelta(hours=+8))).strftime("%H%M")) - 2230) < 30:
            with open("check.json", "r", encoding="utf-8") as checkr_file:
                try:
                    check_data = json.load(checkr_file)
                    first = False
                except json.decoder.JSONDecodeError:
                    first = True
            with open("check.json", "w", encoding="utf-8") as checkw_file:
                if first == True:
                    json.dump({str(msg.author):"True"}, checkw_file, indent=4)
                    first = False
                else:
                    check_data[str(msg.author)] = "True"
                    json.dump(check_data, checkw_file, indent=4)

    @commands.command()
    async def setChannel(self, ctx, channel):
        if ctx.channel == self.channel and ctx.author.id == 776807118481129532:
            self.channel = self.bot.get_channel(int(channel))


def setup(bot):
    bot.add_cog(task(bot))