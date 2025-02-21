#IMPORT LIBRARIES
import discord, datetime
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
from util import embedhelper
from util.logger import log
import os

#DEFINE .ENV OR ELSE NO TOKEN X3
dotenv = load_dotenv('.\\assets\\.env')
if(not dotenv): raise FileNotFoundError

botIntents = discord.Intents.default()
botIntents.message_content = True

watchfox = discord.Bot(intents=botIntents)

@watchfox.event
async def on_ready():
    import datetime
    log(f"Bot started on {str(datetime.date.today())} at {datetime.datetime.now().strftime('%H:%M %p')}")
    log("do i love .....? i do")


watchfox.load_extension('cmds.utils')
watchfox.load_extension('cmds.users')
watchfox.load_extension('cmds.help')
watchfox.load_extension('cmds.fun')
watchfox.load_extension('cmds.misc')


@watchfox.event
async def on_application_command(ctx:discord.ApplicationContext):
    log(f"{ctx.command} was issued by {ctx.author.name} at {datetime.datetime.now()}")
    

@watchfox.event
async def on_application_command_error(
    ctx: discord.ApplicationContext, error: discord.DiscordException):
    from util import exceptionhelper
    _ = exceptionhelper.exceptionEmbed(ctx,error)
    log(str(error))
    await ctx.respond(embed=_)
    await ctx.delete(delay=10)


token = str(os.getenv("TOKEN"))
watchfox.run(token)