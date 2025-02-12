import discord
from discord.ext import commands
from util.logger import log


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.Cog.listener()
    async def on_ready(self):
        log(f'{self.qualified_name} has been loaded')

    fungroup = discord.SlashCommandGroup("fun","fun stuff for entertainment uwu")

    @fungroup.command(name="8ball",description="funny random thingy")
    @commands.cooldown(1,10,commands.BucketType.user)
    async def eightball(self, ctx: discord.ApplicationContext, question:discord.Option(description="ask the eight-ball, mighty traveler")):
        await ctx.defer() 
        from util import embedhelper
        from random import randint
        possibleOutcomes = ["it is vewy likely :3","it's looking promising qwp","give it another try -w-","maybe x3","nu uh it's not looking like it","my best guess is a no","i wont tell you uwu"]
        if(len(question) >= 4):
            _ = embedhelper.createEmbed(embedtitle="the magical ball has spoken!",embeddescription=f"{ctx.author.display_name} asks '{question}{"?" if not question.endswith("?") else ""}'",ctx=ctx)
            _.add_field(name=f"Magical Eight Ball: {possibleOutcomes[randint(0,len(possibleOutcomes)-1)]}",value="")
            await ctx.respond(embed=_)
        else:
            raise ValueError("The question has to be more than 4 characters long, the magical eight-ball fades.")

    @fungroup.command(name="speechbubble",description="creates a speech bubble from an image :sob:")
    @commands.cooldown(1,30,commands.BucketType.user)
    async def speechbubble(self, ctx: discord.ApplicationContext, attachment:discord.Option(discord.SlashCommandOptionType.attachment,description="upload an image",required=False),url:discord.Option(str, "input link",default=None,required=False)):
        await ctx.defer()
        from util import imagehandler,embedhelper
        from PIL import Image
        import pathlib

        if(attachment and url): 
            print("two files sent smh")
            await ctx.respond(content="do not attach 2 files silly smh")
        elif(attachment or url):
            attachment = attachment if not url else url
            tempPath = pathlib.Path('./assets/temp.gif')
            image = imagehandler.overlayBubble(attachment)
            image.save(str(tempPath))
            discordFile = discord.File('./assets/temp.gif','temp.gif')
            _ = embedhelper.createEmbed(embedtitle="",embeddescription="",ctx=ctx)
            _.set_image(url='attachment://temp.gif')
            await ctx.respond(file=discordFile,embed=_)
            image.close()
        else:
            await ctx.respond(content="no attachment provided -w-")

    @fungroup.command(name='rolldice',description='rolls a dice? ;w;')
    @commands.cooldown(1,5,commands.BucketType.user)
    async def rolldice(self, ctx: discord.ApplicationContext, dice:discord.Option(int,required=False, default=6,description="the dice number")):
        await ctx.defer()
        from util import embedhelper
        from random import randint
        listOfDiceNumbers = []
        for x in range(0,randint(50,500)):
            from random import randint
            listOfDiceNumbers.append(str(randint(1,dice)))
        _ = embedhelper.createEmbed(embedtitle=f'rolled a {dice} dice :3',embeddescription="",ctx=ctx)
        _.add_field(name="dice",value=listOfDiceNumbers[randint(0,len(listOfDiceNumbers))])
        await ctx.respond(embed=_)
        listOfDiceNumbers = []

    @fungroup.command(name='flipcoin',description="it flips a coin, either paws(heads) or tails")
    @commands.cooldown(1,5,commands.BucketType.user)
    async def flipcoin(self, ctx:discord.ApplicationContext):
        from random import randint
        from util import embedhelper
        await ctx.defer()
        _ = embedhelper.createEmbed(embedtitle="the coin was flipped!11",embeddescription='',ctx=ctx)
        _.add_field(name='coin',value="tails" if randint(1,500)%2 > 0 else "paws")
        await ctx.respond(embed=_)



def setup(bot):
    bot.add_cog(Fun(bot))