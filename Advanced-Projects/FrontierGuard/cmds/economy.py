import discord, os, json, asyncio, pymongo, random, math
from discord.ext import commands
from pymongo import MongoClient
import requests as re
from datetime import datetime, timezone, timedelta
from core.class_setting import Cog_Extension


class economy(Cog_Extension):
    def data_connect(self):
        cluster = MongoClient("mongodb")
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
            return 1
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
    def ctx_info(self, ctx):
        all_user_displayname = [ctx.guild.members[i].display_name for i in range(len(ctx.guild.members))]
        all_user_id = [ctx.guild.members[i].id for i in range(len(ctx.guild.members))]
        all_user_isbot = [str(ctx.guild.members[i].bot) for i in range(len(ctx.guild.members))]
        return all_user_displayname, all_user_id, all_user_isbot

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
                await ctx.send("Registration Failed! (errorCODE=101)")
            else:
                await add_reaction_message.add_reaction("✔️")
                await add_reaction_message.add_reaction("❌")
                try:
                    await self.bot.wait_for(event="reaction_add",check=check_B, timeout=10)
                except asyncio.TimeoutError:
                    await ctx.send("Registration Failed! (errorCODE=101)")
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
                await ctx.send("Transfer Failed! (errorCODE=101)")
            else:
                await ctx.send("Please input the amount:")
                try:
                    await self.bot.wait_for(event="message",check=check_B, timeout=15)
                except asyncio.TimeoutError:
                    await ctx.send("Transfer Failed! (errorCODE=101)")
                else:
                    if sorf == False:
                        await ctx.send("Transfer Failed! (errorCODE=102)")
                    else:
                        if t == 1:
                            await ctx.send("Successfully transfer money from wallet to bank.")
                        else:
                            await ctx.send("Successfully transfer money from bank to wallet.")
                        await ctx.send("Type \">>deposit\" to get more infomation about your account.")

    @commands.command()
    async def work(self, ctx):
        await ctx.send("Working...")
        collection = self.data_connect()
        result = self.first_set(ctx, collection)       
        if result == 1:
            await ctx.send("You haven't register yet. Type \">>register\" to register.")
        else:
            user_data = collection.find_one({"_id":ctx.author.id})
            if "work" not in user_data or (int(user_data["work"][0]) < int(datetime.now(timezone(timedelta(hours=+8))).strftime("%Y%m%d%H%M%S"))):
                if "work" not in user_data:
                    pass
                elif int(user_data["work"][0]) < int(datetime.now(timezone(timedelta(hours=+8))).strftime("%Y%m%d%H%M%S")):
                    user_data["wallet"] = user_data["wallet"] + user_data["work"][1]
                    await ctx.send(f"Congratulation! You've earn {user_data['work'][1]}$")
                earn = random.randint(150, 250)
                wtime = random.randint(60, 90)
                await ctx.send(f"Start working! You will get {earn}$ after {wtime} minutes.")
                etime = (datetime.now(timezone(timedelta(hours=+8, minutes=wtime)))).strftime("%Y%m%d%H%M%S")
                user_data["work"] = [etime, earn]
                collection.update_one({"_id": ctx.author.id}, {"$set":user_data})
            elif int(user_data["work"][0]) > int(datetime.now(timezone(timedelta(hours=+8))).strftime("%Y%m%d%H%M%S")):
                hr = int(user_data["work"][0][8:10]) - int(datetime.now(timezone(timedelta(hours=+8))).strftime("%Y%m%d%H%M%S")[8:10])
                minn = int(user_data["work"][0][10:12]) - int(datetime.now(timezone(timedelta(hours=+8))).strftime("%Y%m%d%H%M%S")[10:12])
                sec = int(user_data["work"][0][12:]) - int(datetime.now(timezone(timedelta(hours=+8))).strftime("%Y%m%d%H%M%S")[12:])
                tl = [hr, minn, sec]
                if tl[1]<0:
                    tl[0], tl[1] = tl[0]-1, 60+tl[1]
                if tl[2]<0:
                    tl[1], tl[2] = tl[1]-1, 60+tl[2]
                await ctx.send(f"You've already started to work! You will get {user_data['work'][1]}$ after {tl[0]}hr{tl[1]}min{tl[2]}sec.")

    @commands.command()
    async def give(self, ctx, guser, amount):
        try:
            amount = int(amount)
        except BaseException:
            await ctx.send("Please input correct type of amount!")
            return
        guser = str(guser)
        def check_A(reaction, user):
            global rtype
            if user == ctx.author and str(reaction.emoji) == "✔️":
                all_user_displayname, all_user_id, all_user_isbot = self.ctx_info(ctx)
                if guser not in all_user_displayname:
                    rtype = 1
                    return True
                elif all_user_isbot[all_user_displayname.index(guser)] == "True":
                    rtype = 2
                    return True
                elif collection.count_documents({"_id": all_user_id[all_user_displayname.index(guser)]}, limit = 1) == 0:
                    rtype = 3
                    return True
                else:
                    user_data = collection.find_one({"_id":ctx.author.id})
                    if user_data["wallet"] < int(amount):
                        rtype = 4
                        return True
                    else:
                        guser_data = collection.find_one({"_id":all_user_id[all_user_displayname.index(guser)]})
                        if "bank" not in guser_data and "wallet" not in guser_data:
                            user_data["wallet"] -= int(amount)
                            guser_data["bank"] = 0
                            guser_data["wallet"] = int(amount)
                        else:
                            user_data["wallet"] -= int(amount)
                            guser_data["wallet"] += int(amount)
                        collection.update_one({"_id": ctx.author.id}, {"$set":user_data})
                        collection.update_one({"_id": all_user_id[all_user_displayname.index(guser)]}, {"$set":guser_data})
                        rtype = 5
                        return True
            elif user == ctx.author and str(reaction.emoji) == "❌":
                rtype = 6
                return True

        await ctx.send("Working...")
        collection = self.data_connect()
        result = self.first_set(ctx, collection)
        if result == 1:
            await ctx.send("You haven't register yet. Type \">>register\" to register.")
        elif result[0] == 2 or result[1]["bank"] == result[1]["wallet"] == 0:
            await ctx.send("You don't have any $ yet.")
        else:
            await ctx.message.add_reaction("✔️")
            await ctx.message.add_reaction("❌")
            try:
                await self.bot.wait_for(event="reaction_add",check=check_A, timeout=15)
            except asyncio.TimeoutError:
                await ctx.send("Action Failed! (errorCODE=101)")
            else:
                r = [
                    "Is that our guild's member?",
                    "How could you give $ to a robot? Use your brain!",
                    "Is that our guild's member?",
                    "You don't have enough money to give",
                ]
                if 1 <= rtype <= 4:
                    await ctx.send(r[rtype-1])
                elif rtype == 5: 
                    await ctx.send(f"You have successfully give {guser} {amount}$ !")
                else:
                    await ctx.send(f"Action canceled.")

    @commands.command()
    async def rob(self, ctx, typee):
        await ctx.send("Working...")
        collection = self.data_connect()
        result = self.first_set(ctx, collection)
        if result == 1:
            await ctx.send("You haven't register yet. Type \">>register\" to register.")
        else:
            user_data = collection.find_one({"_id":ctx.author.id})
            ranA = [i for i in range(1, 101)]
            if typee == "bank":
                ranB = random.randint(10, 20)
                if random.choice(ranA) <= ranB:
                    ranC = random.randint(2000, 3000)
                    user_data["wallet"] += ranC
                    collection.update_one({"_id": ctx.author.id}, {"$set":user_data})
                    await ctx.send(f"Oh my god! You successfully robbed {ranC}$.")
                else:
                    ranD = random.randint(1000, 1250)
                    user_data["wallet"] -= ranD
                    collection.update_one({"_id": ctx.author.id}, {"$set":user_data})
                    await ctx.send(f"Laugh yourself, You are a loser! And you will be fined {ranD}$.")
            else:
                all_user_displayname, all_user_id, all_user_isbot = self.ctx_info(ctx)
                if typee != ctx.author.name:
                    if typee in all_user_displayname:
                        if all_user_isbot[all_user_displayname.index(typee)] == False:
                            user_data_gf = collection.find_one({"_id":all_user_id[all_user_displayname.index(typee)]})
                            if "bank" in user_data_gf and "wallet" in user_data_gf:
                                if user_data_gf["wallet"] > 100:
                                    ranB = random.randint(30, 40)
                                    if random.choice(ranA) <= ranB:
                                        get = int(math.floor(user_data_gf["wallet"]*0.4))
                                        user_data["wallet"], user_data_gf["wallet"] = user_data["wallet"]+get, user_data_gf["wallet"]-get
                                        collection.update_one({"_id": ctx.author.id}, {"$set":user_data})
                                        collection.update_one({"_id": all_user_id[all_user_displayname.index(typee)]}, {"$set":user_data_gf})
                                        await ctx.send(f"Oh my god! You successfully robbed {typee} {get}$.")
                                    else:
                                        fine = random.randint(500, 750)
                                        await ctx.send(f"Laugh yourself, You are a loser! And you will be fined {fine}$.")
                                        user_data["wallet"] -= fine
                                        if user_data["wallet"] < 0:
                                            user_data["bank"] += user_data["wallet"]
                                            user_data["wallet"] = 0
                                            if user_data["bank"] <= 0:
                                                await ctx.send(f"You are flat broke! Poor you...")
                                                user_data["bank"] = 0
                                        collection.update_one({"_id": ctx.author.id}, {"$set":user_data})
                                else:
                                    await ctx.send(f"{typee} doesn't have enough $ to rob!")
                            else:
                                await ctx.send(f"{typee} doesn't have enough $ to rob!")
                        else:
                            await ctx.send(f"How could you rob a robot? Use your brain!")
                    else:
                        await ctx.send(f"Is that our guild's member?")
                else:
                    await ctx.send(f"How could you rob yourself? Use your brain!")
    
    # @commands.Cog.listener()
    # async def on_message(self, msg):
    #     if msg.content[:11] == ">>interbank" or msg.content[:9] == "tur inter":
    #         await asyncio.sleep(1.5)
    #         API_URL = ""
    #         common_data = re.get(API_URL).json()
    #         if common_data["CtoF"] == {}:
    #             pass
    #         else:
    #             await msg.channel.send("Working...")
    #             cluster = MongoClient("<mongoDB URL>")
    #             database = cluster["database_discordFG"] 
    #             collection = database["collection_discordFG"]
    #             if msg.content[:9] == "tur inter":
    #                 if collection.count_documents({"_id": msg.author.id}, limit = 1) == 0:
    #                     await msg.channel.send("You didn't register here!")
    #                 else:
    #                     user_data = collection.find_one({"_id":msg.author.id})
    #                     user_data["wallet"] += common_data["CtoF"][str(msg.author.id)]
    #                     collection.update_one({"_id": msg.author.id}, {"$set": user_data})
    #                     await msg.channel.send("Action was done!")
    #                     re.post(API_URL, json={"CtoF":{},"FtoC":{}})
    #             if msg.content[:11] == ">>interbank":
    #                 if collection.count_documents({"_id": msg.author.id}, limit = 1) == 0:
    #                     await msg.send("You didn't register here!")
    #                 else:
    #                     user_data = collection.find_one({"_id":msg.author.id})
    #                     if (msg.content[12:]).isdigit() == False:
    #                         await msg.channel.send("Please Input a digit!")
    #                     elif int(msg.content[12:])<=0 or int(msg.content[12:])>=user_data["wallet"]:
    #                         await msg.channel.send("Please Check the range!")
    #                     else:
    #                         user_data["wallet"] -= int(msg.content[12:])
    #                         collection.update_one({"_id": msg.author.id}, {"$set": user_data})
    #                         common_data["FtoC"] = {str(msg.author.id):int(msg.content[12:])}
    #                         re.post(API_URL, json=common_data)
    #                         await msg.channel.send("Action was done!")


def setup(bot):
    bot.add_cog(economy(bot))
