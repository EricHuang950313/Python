import discord, os, json, asyncio, pymongo
from discord.ext import commands
from pymongo import MongoClient
from core.class_setting import Cog_Extension


class economy(Cog_Extension):
    def data_connect(self):
        cluster = MongoClient("mongodb+srv://EricHuang:mongoDBdiscorddatabaseFG@clustera.hm4zc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        database = cluster["database_discordFG"] 
        collection = database["collection_discordFG"]
        return cluster, database, collection
    def data_check_user_exsit(self, ctx):
        cluster, database, collection = self.data_connect()
        if collection.count_documents({"_id": ctx.author.id}, limit = 1) != 0:
            return True, collection.find_one({"_id":ctx.author.id})["name"]
        else:
            return False, False        

    @commands.command()
    async def register(self, ctx):
        def check_A(msg):
            global add_reaction_message
            if msg.content != ("``Account Registration Guide:\n  Step1-Please Input Your Name.\n  Step2-Waiting for generating ✔️ and ❌.\n  Step3-Click: ✔️ for confirm; ❌for cancel.``"):
                add_reaction_message = msg
                return True
        def check_B(reaction, user):
            global addorcancel
            if user == ctx.author and str(reaction.emoji) == "✔️":
                post = {"_id": ctx.author.id, "name": str(add_reaction_message.content)}
                cluster, database, collection = self.data_connect()
                collection.insert_one(post)
                addorcancel = True
                return True
            elif user == ctx.author and str(reaction.emoji) == "❌":
                addorcancel = False
                return True

        await ctx.send("Wait For Checking...")
        exist, name = self.data_check_user_exsit(ctx)
        if exist == True:
            await ctx.send(f"You've already registered! Your name is \"{name}\".")
        else:
            await ctx.send("Start to Register!")
            await ctx.send("``Account Registration Guide:\n  Step1-Please Input Your Name.\n  Step2-Waiting for generating ✔️ and ❌.\n  Step3-Click: ✔️ for confirm; ❌for cancel.``")
            try:
                await self.bot.wait_for(event="message",check=check_A, timeout=30)
            except asyncio.TimeoutError:
                await ctx.send("Registration Failed! (errorCODE=001)")
            else:
                await add_reaction_message.add_reaction("✔️")
                await add_reaction_message.add_reaction("❌")
                try:
                    await self.bot.wait_for(event="reaction_add",check=check_B, timeout=10)
                except asyncio.TimeoutError:
                    await ctx.send("Registration Failed! (errorCODE=001)")
                else:
                    if addorcancel == False:
                        await ctx.send("Registration Canceled!")
                    elif addorcancel == True:
                        await ctx.send("Registration Successfully!")

def setup(bot):
    bot.add_cog(economy(bot))