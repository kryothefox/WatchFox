import yt_dlp,pathlib,discord, threading, asyncio
from util.embedhelper import createEmbed
from util.exceptionhelper import exceptionEmbed


def extractMusicInfo(url):

    ydl_opts = {
    'postprocessors': [
    {
        'key' : 'ReturnYoutubeDislike',
        'when' : "pre_process"
    }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ythandle:
        info = ythandle.extract_info(url,download=False)
        santitized = ythandle.sanitize_info(info,True)
        return santitized







async def getMusicInfo(url,ctx):
        currentLoop = asyncio.get_event_loop()
        thread = await asyncio.to_thread(extractMusicInfo,url)
        return thread


    




async def downloadMusic(url, ctx : discord.ApplicationContext):
    loop = asyncio.get_running_loop()  


    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    },
    {
        'key' : 'ReturnYoutubeDislike',
        'when' : "pre_process"
    },
    ],
    'outtmpl': '%(title)s.%(ext)s',
    } 
    with yt_dlp.YoutubeDL(ydl_opts) as ythandle:
        ythandle.download('url')

