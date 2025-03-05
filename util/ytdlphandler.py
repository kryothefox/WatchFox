import yt_dlp,pathlib

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
    'quiet' : True,
    'outtmpl': '%(title)s.%(ext)s'
}

def getMusicInfo(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ythandle:
        info = ythandle.extract_info(url,download=False)
        santitized = ythandle.sanitize_info(info,True)
        #infoPath = pathlib.Path('./info.json')
        #if(infoPath.exists()): infoPath.unlink() 
        #with open('./info.json','a',encoding='utf-8') as file:
        #    file.write(str(santitized))
        #print(f"{santitized['title']},{santitized['uploader']},{santitized['thumbnail']},{santitized['channel']}") 
        return santitized

