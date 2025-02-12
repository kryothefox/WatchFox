import discord
from discord.ext import commands
from util.logger import log

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        log(f'{self.qualified_name} has been loaded')
    
    miscCommandGroup = discord.SlashCommandGroup(name="misc",description="miscellaneous commands ;w;")

    @miscCommandGroup.command(name="randomcolor",description="sends an embed with random color uwu")
    @commands.cooldown(1,10,commands.BucketType.member)
    async def randomcolor(self ,ctx: discord.ApplicationContext):
        
        from random import randint
        from PIL import Image, ImageColor
        from util import embedhelper
        
        await ctx.defer()
        randomRGBColorArr = []
        for i in range(0,3):
            randomRGBColorArr.append(randint(0,255))
        
        randomColorImage = Image.new("RGB",(500,500),color=tuple(randomRGBColorArr))
        randomColorImage.save('./assets/tempColor.gif')
        colorFile = discord.File('./assets/tempColor.gif','tempColor.gif')
        
        _ = embedhelper.createEmbed(
            embedtitle='let there be colors :3',
            embeddescription="RGB("+", ".join(list(map(str,randomRGBColorArr)))+")",
            ctx=ctx,
            embedcolor=randomRGBColorArr)
        
        _.set_image(url='attachment://tempColor.gif')
        await ctx.respond(file=colorFile, embed=_)
        colorFile.close()
        


def setup(bot):
    bot.add_cog(Misc(bot))