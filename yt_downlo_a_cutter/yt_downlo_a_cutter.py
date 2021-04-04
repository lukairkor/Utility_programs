#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip
import enquiries
import os
from datetime import datetime, date, time, timedelta
import re

# information about video
def video_info(youtube):
    conversion = datetime.timedelta(seconds=youtube.length)
    print('\nVideo description: ', youtube.description)
    print('Rating', youtube.rating)
    print('Length', conversion )
    print('Views', youtube.views, "\n")
    
# downloading video
def down_yt_vid(url, path):
    youtube = pytube.YouTube(url)
    
    video_info(youtube)
    
    video = youtube.streams.filter().first().download(path)
    options = ['Yes', 'No']
    choice = enquiries.choose('Do you want rename file?: ', options)
    if choice == options[0]:    
        print("Enter new name:")
        new_name = input()
        os.rename(video, new_name +'.mp4')
    elif choice == options[1]:  
        pass
    
# downloading only audio   
def down_yt_vid_as_mp3(url, path):
    youtube = pytube.YouTube(url)
    
    video_info(youtube)
        
    video = youtube.streams.filter(only_audio=True).first().download(path)
    options = ['Yes', 'No']
    choice = enquiries.choose('do you want rename file?: ', options)
    if choice == options[0]:    
        print("Enter new name:")
        new_name = input()
        os.rename(video, new_name +'.mp4')
    elif choice == options[1]:       
        pass
    
# convert time from h.m.s to sec
def time_conver(time_tex):
    x = re.findall("[0-9]+", time_tex)
    h = int(x[0]) * 3600
    m = int(x[1]) * 60
    s = int(x[2])

    suma = h + m + s
    return(suma)
    
# cropping video    
def cropp_video(name, path):
    source_path = path + "/" + name
    destin_path = path + "/" + "cropped_"+ name 
    
    clip = VideoFileClip(source_path)
    
    sec = clip.duration
    # mins = (clip.duration % 3600) / 60
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    
    m = str(int(m))
    h = str(int(h))
    s = str(int(s))
    # conversion = datetime.timedelta(seconds=duration)
    print("Duration : "+h+"."+m+"."+s )

    print("\nInput begining and the end of file in seconds")
    print("Begining:")
    start = input()
    start = time_conver(start)

    print("The end:")
    stop = input()
    stop = time_conver(stop)
    
    ffmpeg_extract_subclip(source_path, start, stop/2, targetname = destin_path)
    
# main loop
if __name__ == "__main__":
    path = os.getcwd()
    options = ['Download Video', 'Download only sound', 'Crop file', 'Close']

    while(True):
        os.system('clear')
        choice = enquiries.choose('Choose one of these options: ', options)
        print(choice)
        if choice == options[0]:
            try:
                url = input("Enter url of video")
                down_yt_vid(url, path)
            except:
                print('Try again..')           
        elif choice == options[1]:
            url = input("Enter url of video")
            down_yt_vid_as_mp3(url, path)  
            continue
        elif choice == options[2]:
            name = input("Enter file name:")            
            cropp_video(name, path)
        elif choice == options[3]:
            print("See you soon!")
            break

