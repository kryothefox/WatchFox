import discord, time, datetime
from discord.ext import commands

class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        print(f'{self.qualified_name} has been loaded')
        global startTime
        startTime = time.time()

    @discord.user_command(name="whois",description="returns information about the user >:3")
    @commands.cooldown(1,60,commands.BucketType.user)
    async def whois(self, ctx, member: discord.Member):
        from util import userinfofetch,embedhelper
        userInfo = userinfofetch.getUserInfo(ctx,member)
        _ = embedhelper.createEmbed(f"Who are you, '{member.display_name}'?","",ctx)
        for element in userInfo:
            _.add_field(name=element,value=f"`{userInfo[element]}`",inline=False)
        _.add_field(name="",value="> IP and MAC Address fields are satirical and do not reflect the real values")
        _.set_thumbnail(url=member.avatar.url)
        await ctx.send_response(embed=_)
        
def setup(bot):
    bot.add_cog(Users(bot))