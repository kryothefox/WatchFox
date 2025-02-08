import discord, time, datetime
from discord.ext import commands
from util import embedhelper, getsysteminfo

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    utilgroup = discord.SlashCommandGroup("utility","utility commands for basic debugging tasks or checking if bot alive ;w;", guild_ids=[1309145585701617734])
    debugcmds = utilgroup.create_subgroup("debug","commands for debugging purposes -w-")
    infocmds = utilgroup.create_subgroup("info","commands for debugging purposes -w-")

    @discord.Cog.listener()
    async def on_ready(self):
        print(f'{self.qualified_name} has been loaded')
        global startTime
        startTime = time.time()

    @debugcmds.command(name="ping",description="returns heartbeat latency Owo")
    @commands.cooldown(1,10,commands.BucketType.user)
    async def ping(self, ctx: discord.ApplicationContext):
            _ = embedhelper.createEmbed(embedtitle="Pong?",embeddescription=f"Latency: {round(ctx.bot.latency*1000,ndigits=2)}ms",ctx=ctx)
            await ctx.send_response(embed=_)
    
    @debugcmds.command(name="uptime",description="returns bot uptime :3")
    @commands.cooldown(1,10,commands.BucketType.user)
    async def uptime(self,ctx: discord.ApplicationContext):
        uptime = int(round(datetime.timedelta(seconds=time.time()-startTime).seconds/60))
        _ = embedhelper.createEmbed('Bot Uptime ;w;', f'The bot has been running for {uptime} {"minutes" if uptime != 1 else "minute"}.',ctx)
        _.add_field(name='Start time:',value=time.strftime('%H:%M:%S%p %d-%m-%y',time.localtime(startTime)))
        await ctx.send_response(embed=_)

    @infocmds.command(name="sysinfo",description="returns information about the system the bot is hosted on =w=")
    @commands.cooldown(1,20,commands.BucketType.user)
    async def sysinfo(self,ctx: discord.ApplicationContext):
        _ = embedhelper.createEmbed("System Information ;w;","",ctx)
        systeminfo = getsysteminfo.getSystemInfo()
        for stat in systeminfo:
            _.add_field(name=stat,value=systeminfo[stat],inline=True)
        await ctx.respond(embed=_)
        await ctx.delete(delay=30)



def setup(bot):
    bot.add_cog(Utils(bot))