from util import embedhelper

def exceptionEmbed(ctx,exceptionError):
    embed = embedhelper.createEmbed("Uh-Oh =w=","We ran into a problem executing this command.",ctx,[255,0,0])
    embed.add_field(name="Error:",value=str(exceptionError),inline=False)
    return embed
