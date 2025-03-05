import discord
from discord.ext import commands
from util.logger import log
from util import embedhelper, ytdlphandler, processurl
from util.embedhelper import createEmbed


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        log(f'{self.qualified_name} has been loaded')

    musicCommandGroup = discord.SlashCommandGroup(name="music",description="commands related to music")

    @musicCommandGroup.command(name="getsonginfo",description="gets song info-")
    @commands.cooldown(1,60,commands.BucketType.member)
    async def getsonginfo(self ,ctx: discord.ApplicationContext, url: discord.Option(str,description='the url of the song or video ;w;')):
        import datetime
        await ctx.defer()

        if(not processurl.validateURL(url)): raise ValueError('the inputted URL was not valid ;w;')

        info = ytdlphandler.getMusicInfo(url)
        
        embed = createEmbed(
            embedtitle=f'Song info for "{info['title']}"',
            embeddescription='',
            ctx=ctx)
        embed.set_thumbnail(url=info['thumbnail'])

        if(info['duration_string']): embed.add_field(name='Duration',value=f'{info['duration_string']}',inline=False)
        if(info['uploader']): embed.add_field(name='Uploader',value=f'{info['uploader']}',inline=False)
        if(info['timestamp']): embed.add_field(name='Time of creation', value=f"{datetime.datetime.fromtimestamp(info['timestamp']).strftime("%H:%M - %d %b %Y")}",inline=False)
        if(info['view_count']): embed.add_field(name='Views',value=f"{info['view_count']}",inline=True)
        if(info['comment_count']): embed.add_field(name='Comments',value=f"{info['comment_count']}",inline=True)
        if(info['like_count']): embed.add_field(name='Likes',value=f"{info['like_count']}",inline=True)
        
        if (info['extractor_key'] == "Youtube"): 
            if(info['dislike_count']):
                 embed.add_field(name='Dislikes',value=f"{info['dislike_count']}",inline=True)

        await ctx.respond(embed=embed)



def setup(bot):
    bot.add_cog(Music(bot))