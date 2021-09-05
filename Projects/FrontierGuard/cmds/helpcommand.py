import discord, json, asyncio
from discord.ext import commands
from googletrans import Translator
from core.class_setting import Cog_Extension

with open("help_info.json", "r", encoding="utf8") as j_file:
    j_data = json.load(j_file)
    
class helpcommand(Cog_Extension):
    def getContent(self, typee, embed, t):
        if typee == "":
            typee = "general" 
        for i in range(len(j_data[typee]["name"])):
            if t == 1:
                translator = Translator()
                if typee == "general":
                    embed.add_field(name=j_data[typee]["name"][i][0:3]+translator.translate(j_data[typee]["name"][i][3:], dest="zh-tw").text, value=j_data[typee]["content"][i], inline=False)
                else:
                    embed.add_field(name=j_data[typee]["name"][i], value=translator.translate(j_data[typee]["content"][i], dest="zh-tw").text, inline=False)
            else:
                embed.add_field(name=j_data[typee]["name"][i], value=j_data[typee]["content"][i], inline=False)
        return embed

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        if ctx.message.content[7:] not in ["tba", "eco", "ency", "pic", "eC", ""]:
            await ctx.send("Command NOT FOUND! (errorCODE=001)")
            await ctx.send("Try\">>help\" for checking commands.")
        else:
            def lang(reaction, user):
                if user == ctx.author and str(reaction.emoji) == "🇨":
                    return 1
            await ctx.message.add_reaction("🇨")
            embed=discord.Embed(title=j_data["title"][(lambda a: "general" if a == "" else a)(ctx.message.content[7:])], description=(lambda a: "\">>help\" command helps you easily get hang of using the bot." if a == "" else "")(ctx.message.content[7:]), color=0xffca57)
            embed = self.getContent(ctx.message.content[7:], embed, 0)
            fr = await ctx.send(embed=embed)
            while True:
                try:
                    r, m = await self.bot.wait_for(event="reaction_add",check=lang, timeout=30)
                except asyncio.TimeoutError:
                    await ctx.message.clear_reactions() 
                    break
                if r.emoji == "🇨"  and r.count == 2 and m == ctx.message.author:
                    embed=discord.Embed(title=j_data["title"][(lambda a: "general" if a == "" else a)(ctx.message.content[7:])], description=(lambda a: "\">>help\" command helps you easily get hang of using the bot." if a == "" else "")(ctx.message.content[7:]), color=0xffca57)
                    await ctx.message.clear_reactions()
                    embed = self.getContent(ctx.message.content[7:], embed, 1)
                    await fr.edit(embed=embed)         
                      

def setup(bot):
    bot.add_cog(helpcommand(bot))