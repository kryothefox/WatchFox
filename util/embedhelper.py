import discord
import os, dotenv
dotenv.load_dotenv(".\\assets\\.env")
ver  = str(os.getenv("ver"))

def createEmbed(embedtitle, embeddescription, ctx, embedcolor=[180, 190, 254]):
    try:
        embed = discord.Embed(
            title=embedtitle,
            description=embeddescription,
            color=discord.Colour.from_rgb(embedcolor[0],embedcolor[1],embedcolor[2]),
        )
        embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar.url)
        embed.set_footer(text=f"WatchFox version {ver}",icon_url=ctx.bot.user.avatar.url)
        return embed
    except:
        raise Exception