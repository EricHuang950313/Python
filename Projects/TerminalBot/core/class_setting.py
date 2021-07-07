import discord
from discord.ext import commands


class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        Cog_Extension._aa = []
        Cog_Extension._bb = []
        Cog_Extension._statusaa = False
        Cog_Extension._statusbb = False