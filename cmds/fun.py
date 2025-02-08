import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.Cog.listener()
    async def on_ready(self):
        print(f'{self.qualified_name} has been loaded')

    fungroup = discord.SlashCommandGroup("fun","fun stuff for entertainment uwu")

    @fungroup.command(name="8ball",description="funny random thingy")
    @commands.cooldown(1,10,commands.BucketType.user)
    async def eightball(self,ctx: discord.ApplicationContext, question:discord.Option(description="ask the eight-ball, mighty traveler")):
        from util import embedhelper
        from random import randint
        possibleOutcomes = ["it is vewy likely :3","it's looking promising qwp","give it another try -w-","maybe x3","nu uh it's not looking like it","my best guess is a no","i wont tell you uwu"]
        if(len(question) > 4):
            _ = embedhelper.createEmbed(embedtitle="the magical ball has spoken!",embeddescription=f"{ctx.author.display_name} asks '{question}{"?" if not question.endswith("?") else ""}'",ctx=ctx)
            _.add_field(name=f"Magical Eight Ball: {possibleOutcomes[randint(0,len(possibleOutcomes)-1)]}",value="")
            await ctx.respond(embed=_)
        else:
            raise ValueError("The question has to be more than 4 characters long, the magical eight-ball fades.")

def setup(bot):
    bot.add_cog(Fun(bot))