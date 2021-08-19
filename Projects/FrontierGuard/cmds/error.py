import discord
from discord.ext import commands
from core.class_setting import Cog_Extension


class error(Cog_Extension):
    # Global Exception Handling
    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        # Checking if Individual Command Exception Handling exist.
        # if hasattr(ctx.command, "on_error"):
        #     return
        if isinstance(exception, commands.errors.CommandNotFound):
            await ctx.send("Command NOT FOUND! (errorCODE=001)")
            await ctx.send("Try\">>help\" for checking commands.")
        else:
            await ctx.send("Exception! (errorCODE=002)")
            await ctx.send("This is a exception that is out of except.")
            await ctx.send("Please take a screenshot, describe the situation and send them to the following email:")
            await ctx.send("songzhi313@gmail.com")
    
    # Individual Command Exception Handling
    # from [folders_name].[file_name] import [file_class_name] if "@test.error" and "@commands.command()" in different file.
    # e.g from cmds.text import text if "@test.error" in cmds/error.py and "@commands.command()" in cmds/text.py, and use decorator as "@text.test.error"
    # @commands.command()
    # async def test(self, ctx, a):
    #     await ctx.send(a+1)  
    # @test.error
    # async def test_error(self, ctx, exception):
    #     if isinstance(exception, commands.errors.MissingRequiredArgument):
    #         await ctx.send("test: Missing required argument!")
        
def setup(bot):
    bot.add_cog(error(bot))