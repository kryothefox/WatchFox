import discord, time, datetime
from discord.ext import commands
from util import embedhelper, getsysteminfo

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    


    



    
def setup(bot):
    bot.add_cog(Help(bot))