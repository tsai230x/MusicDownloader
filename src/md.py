import tkinter as tk
from tkinter import filedialog
import ssl
import os
from bs4 import BeautifulSoup
import requests
from pytube import YouTube

ssl._create_default_https_context = ssl._create_stdlib_context

def Download():
    os.chdir(dir.get())

    yt = YouTube(url.get())

    title = GetTitle()
    
    yt.streams.filter(only_audio=True,abr='128kbps').get_audio_only().download(filename=f'{title}.mp3')

    status.config(text='OK!',fg='green')

def OpenFile():
    dirSel=filedialog.askdirectory()
    dir.set(dirSel)

def GetTitle():
    html = requests.get(url.get())
    html.encoding = 'UTF-8'
    sp = BeautifulSoup(html.text,'lxml')
    title = sp.find('meta',itemprop='name')['content']
    
    return title

def DownloadCheck():
    dirStatus=False
    urlStatus=False
    if(dir.get()!=''):
        dirStatus=True
    else:
        dirStatus=False
    if(url.get()!=''):
        urlStatus=True
    else:
        urlStatus=False
    if((urlStatus==False) and (dirStatus==False)):
        status.config(text='Youtube連結、儲存位置不得為空',fg='red')
    elif(urlStatus==False):
        status.config(text='Youtube連結不得為空',fg='red')
    elif(dirStatus==False):
        status.config(text='儲存位置不得為空',fg='red')
    else:
        Download()

MainWin=tk.Tk()
MainWin.title('EZ Music Downloader')
MainWin.geometry('340x150')

url=tk.StringVar()
urlLabel=tk.Label(text='YouTube連結:')
urlEntry=tk.Entry(textvariable=url)
urlLabel.place(x=10,y=10)
urlEntry.place(x=100,y=10)

dir=tk.StringVar()
dirLabel=tk.Label(text='儲存位置:')
dirEntry=tk.Entry(textvariable=dir)
dirBtn=tk.Button(text='選擇路徑',command=OpenFile)
dirLabel.place(x=10,y=60)
dirEntry.place(x=100,y=60)
dirBtn.place(x=250,y=60)

DownloadBtn=tk.Button(text='下載',command=DownloadCheck)
DownloadBtn.place(x=10,y=110)

status=tk.Label(text='',fg='black',font=20)
status.place(x=75,y=110)

#TestBtn=tk.Button(text='測試',command=Test)
#TestBtn.pack()

MainWin.mainloop()