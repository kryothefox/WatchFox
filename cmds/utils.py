import discord, time, datetime
from discord.ext import commands
from util import *

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    utilgroup = discord.SlashCommandGroup("utility","utility commands for basic debugging tasks or checking if bot alive ;w;")
    debugcmds = utilgroup.create_subgroup("debug","commands for debugging purposes -w-")

    @discord.Cog.listener()
    async def on_ready(self):
        print(f'{self.qualified_name} has been loaded')
        global startTime
        startTime = time.time()

    
    
    @debugcmds.command(name="ping",description="returns heartbeat latency Owo")
    @commands.cooldown(1,10,commands.BucketType.user)
    async def ping(self, ctx: discord.ApplicationContext):
            _ = embedhelper.createEmbed(embedtitle="Pong?",embeddescription=f"Latency: {round(ctx.bot.latency,4)*1000}ms",ctx=ctx)
            await ctx.send_response(embed=_)
    
    @debugcmds.command(name="uptime",description="returns bot uptime :3")
    @commands.cooldown(1,10,commands.BucketType.user)
    async def uptime(self,ctx: discord.ApplicationContext):
        _ = embedhelper.createEmbed('Bot Uptime', f'The bot has been running for {datetime.timedelta(seconds=int(round(time.time()-startTime))).seconds} second(s)',ctx)
        _.add_field(name='Start time:',value=time.strftime('%H:%M:%S%p %d-%m-%y',time.localtime(startTime)))
        await ctx.send_response(embed=_)





def setup(bot):
    bot.add_cog(Utils(bot))