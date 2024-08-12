import tkinter as tk
from tkinter import filedialog
import ssl
import os
from bs4 import BeautifulSoup
import requests
import lxml
from pytube import YouTube

ssl._create_default_https_context = ssl._create_stdlib_context

def Download():
    if(dir.get()==''):
        os.chdir('E:\Music')
    else:
        os.chdir(dir.get())

    yt = YouTube(url.get())

    #print("可用的音頻流:")
    #for stream in yt.streams.filter(only_audio=True,abr='128kbps'):
    #    print(f"音質: {stream.abr}, 格式: {stream.mime_type}, 擴展名: {stream.subtype}")

    print('download...')
    yt.streams.filter(only_audio=True,abr='128kbps').get_audio_only().download(filename=yt.title+'.mp3')

    print('ok!')

def OpenFile():
    dirSel=filedialog.askdirectory()
    dir.set(dirSel)

def GetTitle():
    html = requests.get(url.get())
    html.encoding = 'UTF-8'
    sp = BeautifulSoup(html.text,'lxml')
    title = sp.find('meta',itemprop='name')['content']
    print(title)
    
    #return sp.yt-formatted-string.text

MainWin=tk.Tk()
MainWin.title('EZ Music Downloader')
MainWin.geometry('360x150')

dir=tk.StringVar()
dirLabel=tk.Label(text='儲存位置:')
dirEntry=tk.Entry(textvariable=dir)
dirBtn=tk.Button(text='選擇路徑',command=OpenFile)
dirLabel.pack()
dirEntry.pack()
dirBtn.pack()

url=tk.StringVar()
urlLabel=tk.Label(text='YouTube連結:')
urlEntry=tk.Entry(textvariable=url)
urlLabel.pack()
urlEntry.pack()

DownloadBtn=tk.Button(text='下載',command=Download)
DownloadBtn.pack()

TestBtn=tk.Button(text='測試',command=GetTitle)
TestBtn.pack()

MainWin.mainloop()