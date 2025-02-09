import discord
from discord.ext import commands
from util.logger import log


class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        log(f'{self.qualified_name} has been loaded')

    usergroup = discord.SlashCommandGroup("users","useful commands for user interactions like profiles")
    

    @usergroup.command(name="whois",description="returns information about the user >:3")
    @commands.cooldown(1,60,commands.BucketType.user)
    async def whois(self, ctx:discord.ApplicationContext, member: discord.Member):
        await ctx.defer()
        from util import userinfofetch,embedhelper
        userInfo = userinfofetch.getUserInfo(ctx,member)
        _ = embedhelper.createEmbed(f"Who are you, '{member.display_name}'?","",ctx)
        for element in userInfo:
            _.add_field(name=element,value=f"`{userInfo[element]}`",inline=False)
        _.add_field(name="",value="> IP and MAC Address fields are satirical and do not reflect the real values")
        _.add_field(name="",value="Due to message length, this message will be deleted after 60 seconds upon issue.")
        _.set_thumbnail(url=member.avatar.url)
        await ctx.respond(embed=_)
        await ctx.delete(delay=10)
    
    @usergroup.command(name="getavatar", description="gets avatar of the user >:3")
    @commands.cooldown(1,30,commands.BucketType.user)
    async def getavatar(self,ctx:discord.ApplicationContext, member:discord.Member):
        await ctx.defer()
        from util import embedhelper
        _ = embedhelper.createEmbed(f"Avatar of {member.display_name}","",ctx)
        _.set_image(url=member.avatar.url)
        await ctx.respond(embed=_)
    
    @usergroup.command(name="accountage",description="returns the account age of the user")
    @commands.cooldown(1,10,commands.BucketType.user)
    async def accountage(self, ctx:discord.ApplicationContext, member:discord.Member):
        await ctx.defer()
        from util import embedhelper, userinfofetch
        age = userinfofetch.getAge(member).days
        _ = embedhelper.createEmbed(f"Account age for {member.display_name}","",ctx)
        _.set_thumbnail(url=member.avatar.url)
        _.add_field(name=f"This account is {age} days old!",value="",inline=False)
        _.add_field(name=f"",value=f"created at {member.created_at}")
        await ctx.respond(embed=_)
        
    
        
def setup(bot):
    bot.add_cog(Users(bot))