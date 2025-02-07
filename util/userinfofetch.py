import discord, time, datetime
from discord.ext import commands

def getUserInfo(ctx, member):
    from random import randint
    userInfo = {
        "Username" : member.name,
        "Global Name" : member.global_name,
        "Display Name" : member.display_name,
        "Account Created At" : member.created_at,
        "User ID" : member.id,
        "Status" : str(member.status),
        "Avatar Url" : member.avatar.url,
        "Is Open To DMs" : member.can_send(),
        "IP" : f"{randint(1,255)}.{randint(1,255)}.{randint(1,255)}.{randint(1,255)}", # :3333
        "Device MAC Address" : f"{chr(randint(65,70))}{chr(randint(65,70))}:{chr(randint(48,57))}{chr(randint(48,57))}:{chr(randint(65,70))}{chr(randint(65,70))}:{chr(randint(48,57))}{chr(randint(65,70))}:{chr(randint(48,57))}{chr(randint(65,70))}:{chr(randint(65,70))}{chr(randint(48,57))}",
    }
    return userInfo
    


