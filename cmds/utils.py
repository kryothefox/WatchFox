import discord
from discord.ext import commands
from util import *

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="ping",description="returns heartbeat latency Owo", cooldown=discord())
    async def ping(self, ctx: discord.ApplicationContext):
        try:
            cmdembed = embedhelper.createEmbed(embedtitle="Pong?",embeddescription=f"Latency: {round(ctx.bot.latency,4)*1000}ms",ctx=ctx)
            await ctx.send_response(embed=cmdembed)
        except Exception as e:
            exceptionEmbed = exceptionhelper.exceptionEmbed(ctx,e)
            await ctx.send_response(embed=exceptionEmbed)

def setup(bot):
    bot.add_cog(Utils(bot))