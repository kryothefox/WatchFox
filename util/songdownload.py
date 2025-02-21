import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'outtmpl': '%(title)s.%(ext)s'
}


with yt_dlp.YoutubeDL(ydl_opts) as ythandle:
    dl = ythandle.download(url_list=['https://soundcloud.com/xaxaxaxaxaxaxaxaxaaxa/the-living-tombstone-cats-sped-up'])
    