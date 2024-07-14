import tkinter as tk
import ssl
import os
from pytube import YouTube


ssl._create_default_https_context = ssl._create_stdlib_context

def Run():
    os.chdir(dir.get())

    yt = YouTube(url.get())

    #print("可用的音頻流:")
    #for stream in yt.streams.filter(only_audio=True,abr='128kbps'):
    #    print(f"音質: {stream.abr}, 格式: {stream.mime_type}, 擴展名: {stream.subtype}")

    print('download...')
    yt.streams.filter(only_audio=True,abr='128kbps').get_audio_only().download(filename=yt.author+' - '+yt.title+'.mp3')

    print('ok!')

winmd=tk.Tk()
winmd.title('EZ Music Downloader')

url=tk.StringVar()
label1=tk.Label(text='YouTube連結:')
entry1=tk.Entry(textvariable=url)
label1.pack()
entry1.pack()

dir=tk.StringVar()
label2=tk.Label(text='儲存位置:')
entry2=tk.Entry(textvariable=dir)
label2.pack()
entry2.pack()

button1=tk.Button(text='下載',command=Run)
button1.pack()

winmd.mainloop()