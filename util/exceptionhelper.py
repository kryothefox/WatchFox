from util import embedhelper

def exceptionEmbed(ctx,exceptionError):
    embed = embedhelper.createEmbed("Ow Nou :c","I ran into a problem executing this command.",ctx,[255,0,0])
    embed.add_field(name="Error:",value=str(exceptionError),inline=False)
    embed.set_footer("This message will delete in 10 seconds")
    return embed
