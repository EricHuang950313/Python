import discord, json, asyncio, requests
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

        async def update():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(855062319435087872)
            while not self.bot.is_closed():
                if datetime.now(timezone(timedelta(hours=+8))).strftime("%H%M%S") == "120005" or datetime.now(timezone(timedelta(hours=+8))).strftime("%H%M%S") == "000005":
                    API_URL = "https://getpantry.cloud/apiv1/pantry/4feb1fac-6e16-4e25-9b43-12d4a2b7df5e/basket/discord_frontierguard"
                    response = requests.get(API_URL)
                    new_data = {"record": 0, "FrontierGuard#5696": True}
                    update = requests.post(API_URL, json=new_data)
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
        self.backgroundTb = self.bot.loop.create_task(update())

    @commands.Cog.listener()
    async def on_message(self, msg):
        time = int(datetime.now(timezone(timedelta(hours=+8))).strftime("%H%M"))
        content = [["Goodmorning", "早安", "おはようございます"], ["Goodnight", "晚安", "おやすみなさい"]]
        if (time > 600 and time < 1200 or time > 2000) and (msg.content in content[0] or msg.content in content[1]):
            API_URL = "https://getpantry.cloud/apiv1/pantry/4feb1fac-6e16-4e25-9b43-12d4a2b7df5e/basket/discord_frontierguard"
            DIGIT_LIST = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
            response = requests.get(API_URL)
            data = response.json()
            for author in data:
                if author == str(msg.author):
                    break
            else:
                if data["record"] == 0 and msg.content in content[0] and time > 600 and time < 1200:
                    await msg.add_reaction("👑")
                    await msg.channel.send("Goodmorning! 早安! おはようございます! ")
                    data["record"] = 1 
                    data[str(msg.author)] = True
                elif data["record"] == 0 and msg.content in content[1] and time > 2000:
                    await msg.add_reaction("👑")
                    await msg.channel.send("Goodnight! 晚安! おやすみなさい! ")
                    data["record"] = 1 
                    data[str(msg.author)] = True
                elif data["record"] == 10:
                    data["record"] = data["record"] + 1
                    data[str(msg.author)] = True
                    await msg.add_reaction(DIGIT_LIST[1])
                    await msg.add_reaction(DIGIT_LIST[0])
                elif (msg.content in content[0] and time > 600 and time < 1200) or (msg.content in content[1] and time > 2000):
                    data["record"] = data["record"] + 1
                    data[str(msg.author)] = True
                    if len(str(data["record"])) == 1:
                        await msg.add_reaction(DIGIT_LIST[0])
                        await msg.add_reaction(DIGIT_LIST[data["record"]])
                    else:
                        pass
                update = requests.post(API_URL, json=data)
        else:
            pass

    @commands.command()
    async def setChannel(self, ctx, channel):
        if ctx.channel == self.channel and ctx.author.id == 776807118481129532:
            self.channel = self.bot.get_channel(int(channel))


def setup(bot):
    bot.add_cog(task(bot))