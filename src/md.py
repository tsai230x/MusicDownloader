import tkinter
tk=tkinter.Tk()
tk.title('Music Downloader')
#tk.mainloop()

import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

import os
os.chdir('E:\Music')

from pytube import YouTube
yt = YouTube('https://youtu.be/rmoKxuP_bsI?si=sRet-e9v1B9iHNkN')

#print("可用的音頻流:")
#for stream in yt.streams.filter(only_audio=True,abr='128kbps'):
#    print(f"音質: {stream.abr}, 格式: {stream.mime_type}, 擴展名: {stream.subtype}")

print('download...')
yt.streams.filter(only_audio=True,abr='128kbps').get_audio_only().download(filename=yt.author+' - '+yt.title+'.mp3')

print('ok!')