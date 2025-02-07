#IMPORT LIBRARIES
import discord 
from discord.ext import commands
from dotenv import load_dotenv
from util import embedhelper, exceptionhelper
import os
#DEFINE .ENV OR ELSE NO TOKEN X3
dotenv = load_dotenv('.\\assets\\.env')
if(not dotenv): raise FileNotFoundError

watchfox = discord.Bot()

@watchfox.event
async def on_ready():
    print("i love cocks")

watchfox.load_extension('cmds.utils')



token  = str(os.getenv("TOKEN"))
watchfox.run(token)