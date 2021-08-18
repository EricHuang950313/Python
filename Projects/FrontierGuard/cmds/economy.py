import discord, os, json, asyncio, pymongo
from discord.ext import commands
from pymongo import MongoClient
from core.class_setting import Cog_Extension


class economy(Cog_Extension):
    def data_connect(self):
        cluster = MongoClient("<mongoDB URL>")
        database = cluster["database_discordFG"] 
        collection = database["collection_discordFG"]
        return collection
    def data_check_user_exsit(self, ctx, collection):
        if collection.count_documents({"_id": ctx.author.id}, limit = 1) != 0:
            return True, collection.find_one({"_id":ctx.author.id})["name"]
        else:
            return False, False   
    def first_set(self, ctx, collection):
        if self.data_check_user_exsit(ctx, collection) == (False, False):
            return 1, None
        else:
            user_data = collection.find_one({"_id":ctx.author.id})
            if "bank" and "wallet" not in user_data:
                user_data["bank"] = 0
                user_data["wallet"] = 0
                collection.update_one({"_id": ctx.author.id}, {"$set":user_data})
                user_data = collection.find_one({"_id":ctx.author.id})
                return 2, user_data
            else:
                return 3, user_data

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
                collection.insert_one(post)
                addorcancel = True
                return True
            elif user == ctx.author and str(reaction.emoji) == "❌":
                addorcancel = False
                return True
        await ctx.send("Wait For Checking...")
        collection = self.data_connect()        
        exist, name = self.data_check_user_exsit(ctx, collection)
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

    @commands.command()
    async def deposit(self, ctx):
        await ctx.send("Working...")
        collection = self.data_connect()
        result = self.first_set(ctx, collection)
        if result == 1:
            await ctx.send("You haven't register yet. Type \">>register\" to register.")
        elif result[0] == 2:
            await ctx.send(f"User Name: {result[1]['name']} | Bank: {result[1]['bank']}$ | Wallet: {result[1]['wallet']}$")
        else:
            await ctx.send(f"User Name: {result[1]['name']} | Bank: {result[1]['bank']}$ | Wallet: {result[1]['wallet']}$")
    
    @commands.command()
    async def to(self, ctx):
        def check_A(reaction, user):
            global types
            if user == ctx.author and str(reaction.emoji) == "🇧":
                types = "B"
                return True
            elif user == ctx.author and str(reaction.emoji) == "🇼":
                types = "W"
                return True
        def check_B(msg):
            global sorf, t
            if str(msg.content).isdigit() == False:
                (sorf, t) = False, None
            elif int(msg.content) <= 0:
                (sorf, t) = False, None
            else:
                user_data = collection.find_one({"_id":ctx.author.id})
                bank, wallet, value = user_data["bank"], user_data["wallet"], int(msg.content)
                if types == "B":
                    if value > wallet:
                        (sorf, t) = False, None
                    else:
                        bank, wallet = bank+value, wallet-value
                        user_data["bank"], user_data["wallet"] = bank, wallet
                        collection.update_one({"_id": ctx.author.id}, {"$set":user_data})
                        (sorf, t) = True, 1
                elif types == "W":
                    if value > bank:
                        (sorf, t) = False, None
                    else:
                        bank, wallet = bank-value, wallet+value
                        user_data["bank"], user_data["wallet"] = bank, wallet
                        collection.update_one({"_id": ctx.author.id}, {"$set":user_data})
                        (sorf, t) = True, 2
            return True

        await ctx.send("Working...")
        collection = self.data_connect()
        result = self.first_set(ctx, collection)
        if result == 1:
            await ctx.send("You haven't register yet. Type \">>register\" to register.")
        elif result[0] == 2 or result[1]["bank"] == result[1]["wallet"] == 0:
            await ctx.send("You don't have any $ yet.")
        else:
            await ctx.send("🇧 -> ToBank | 🇼 -> ToWallet")
            await ctx.message.add_reaction("🇧")
            await ctx.message.add_reaction("🇼")
            try:
                await self.bot.wait_for(event="reaction_add",check=check_A, timeout=15)
            except asyncio.TimeoutError:
                await ctx.send("Transfer Failed! (errorCODE=001)")
            else:
                await ctx.send("Please input the amount:")
                try:
                    await self.bot.wait_for(event="message",check=check_B, timeout=15)
                except asyncio.TimeoutError:
                    await ctx.send("Transfer Failed! (errorCODE=001)")
                else:
                    if sorf == False:
                        await ctx.send("Transfer Failed! (errorCODE=002)")
                    else:
                        if t == 1:
                            await ctx.send("Successfully transfer money from wallet to bank.")
                        else:
                            await ctx.send("Successfully transfer money from bank to wallet.")
                        await ctx.send("Type \">>deposit\" to get more infomation about your account.")

           
def setup(bot):
    bot.add_cog(economy(bot))