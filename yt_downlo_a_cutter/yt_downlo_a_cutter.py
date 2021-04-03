#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip
import enquiries
import os

# information about video
def video_info(youtube):
    print('\nvideo description: ', youtube.description)
    print('rating', youtube.rating)
    print('length', youtube.length)
    print('views', youtube.views, "\n")
    
# downloading video
def down_yt_vid(url, path):
    youtube = pytube.YouTube(url)
    
    video_info(youtube)
    
    video = youtube.streams.filter().first().download(path)
    options = ['Yes', 'No']
    choice = enquiries.choose('do you want rename file?: ', options)
    if choice == options[0]:    
        print("enter new name:")
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
        print("enter new name:")
        new_name = input()
        os.rename(video, new_name +'.mp4')
    elif choice == options[1]:  
        pass
    
# cropping video    
def cropp_video(name, path):
    source_path = path + "/" + name
    destin_path = path + "/" + "cropped_"+ name 
    
    clip = VideoFileClip(source_path)
    duration = clip.duration
    print("Duration : " + str(duration) +" second")
    
    print("\nInput begining and the end of file in seconds")
    print("begining:")
    start = int(input())
    print("The end:")
    stop = int(input())
    
    ffmpeg_extract_subclip(source_path, start, stop, targetname = destin_path)
    
# main loop
if __name__ == "__main__":
    path = os.getcwd()
    options = ['Download YT Video', 'Download YT Video_as_mp3', 'crop file', 'Aby zakończyć']

    while(True):
        os.system('clear')
        choice = enquiries.choose('Choose one of these options: ', options)
        print(choice)
        if choice == options[0]:
            print("enter url of video")
            url = input()
            down_yt_vid(url, path)
            continue
        elif choice == options[1]:
            print("enter url of video")
            url = input()
            down_yt_vid_as_mp3(url, path)  
            continue
        elif choice == options[2]:
            print("enter file name:")
            name = input()            
            cropp_video(name, path)
        elif choice == options[3]:
            print("see you soon!")
            break
        else:
            print("try again")
            os.system('clear')
