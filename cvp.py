# -*- coding: utf-8 -*-
from Tanlan.Tanlan import *
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz,  urllib, urllib.parse,timeit,atexit,youtube_dl,pafy
print("""
登入選單
Qr=1
Token=2
Gmail=3
""")
what = input("請輸入您要登入的模式代碼:")
if what == "1":
    client = LINE()
if what == "2":
    tok= input("請輸入您要登入的Token:")
    client = LINE(tok)
if what == "3":
    tokg= input("請輸入您要登入的Gmail:")
    tokp= input("請輸入您要登入的Password:")
    client = LINE(tokg,tokp)
oepoll = OEPoll(client)
print("login")
def ytdl(url):
    video = pafy.new(url)
    best = video.getbest() 
    best.download(filepath="test.mp4")
wait = {
    'group': "",
    'cvp': False,#更換頭貼
    }
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                if op.type == 25:
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    if msg.contentType == 1:
                        if wait["group"] == msg.to:
                            if wait["cvp"] == True:
                                while True:
                                    try:
                                        image = client.downloadObjectMsg(msg_id, saveAs="cvp.jpg")
                                        if os.path.isfile(image):
                                            break
                                    except:
                                        continue
                                client.sendMessage(msg.to, "圖片下載完成 正在更換頭貼(｡･ω･｡)")
                                wait["cvp"] = False
                                client.updateVideoAndPictureProfile("test.mp4",image)
                                os.remove("test.mp4")
                                os.remove(image)
                                client.sendMessage(msg.to, "更改完成 已登出機器(｡･ω･｡)")
                                client.logout()
                    if msg.contentType == 0:
                        if msg.text.startswith("Cvp:"):
                            search = msg.text.replace("Cvp:","")
                            ytdl(search)
                            client.sendMessage(msg.to, "影片下載完成 請傳送圖片")
                            wait["cvp"] = True
                            wait["group"] = msg.to
    except Exception as e:
        print (e)