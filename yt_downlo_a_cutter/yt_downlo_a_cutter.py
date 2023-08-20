#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
- youtube downloader
- cropping video
'''
import datetime
import os
import re
import subprocess
import sys
from os.path import isfile, join

import enquiries
import inquirer
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from pytube import YouTube, exceptions


# from os import listdir


def get_video_info(youtu):
    '''Get information about a video, choose a resolution, and return the worked itag.'''

    unique_resolutions = set()  # Keep track of unique resolutions
    resolution_choices = []  # Prepare the list of resolution choices

    for stream in youtu.streams:
        if stream.mime_type == "video/mp4" and stream.resolution not in unique_resolutions:
            unique_resolutions.add(stream.resolution)
            resolution_choices.append(f"{stream.resolution} ({stream.mime_type})")

    if not resolution_choices:
        print("No .mp4 streams available.")
        return None

    # Sort the resolution choices in ascending order
    resolution_choices.sort()

    print('\nVideo description:', youtu.description)
    print('Rating:', youtu.rating)
    print('Length:', datetime.timedelta(seconds=youtu.length))
    print('Views:', youtu.views, "\n")

    # Define the available options for resolutions using inquirer
    options = [
        inquirer.List('resolution',
                      message='Choose a resolution:',
                      choices=resolution_choices,
                      carousel=True)
    ]

    # Prompt user to choose a resolution
    answers = inquirer.prompt(options)

    chosen_resolution = answers['resolution']
    chosen_stream = next(
        (stream for stream in youtu.streams if f"{stream.resolution} ({stream.mime_type})" == chosen_resolution), None)

    if chosen_stream:
        return chosen_stream  # Return the chosen stream directly
    else:
        print("Invalid choice. Returning None...")
        return None


def progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    # Print progress more frequently
    if percentage % 10 == 0:
        print(f"Downloaded: {percentage:.2f}%")
    print(f"Downloaded: {percentage:.2f}%")


def down_yt_vid(youtu, video_path, kind):
    '''downloading video'''
    extension = 'mp4'

    options = ['Yes', 'No']
    choice = enquiries.choose('Do you want preview file?: ', options)
    if choice == options[0]:
        video_play(youtu)
    elif choice == options[1]:
        pass

    if kind == 0:
        video = youtu.streams.filter(file_extension=extension).first()
        video.download(video_path)
    elif kind == 1:
        video = youtu.streams.filter(only_audio=True).first()
        video.download(video_path)
    rename_file(video)


def rename_file(video):
    '''rename file'''
    options = ['Yes', 'No']
    choice = enquiries.choose('Do you want rename file?: ', options)
    if choice == options[0]:
        video_name = input("Enter new name (without extension):\n")
        original_filename = video.default_filename
        old_name = os.path.join(os.getcwd() + "/" + str(original_filename))
        new_name = os.path.join(os.getcwd(), video_name + '.mp4')
        print(new_name)
        os.rename(old_name, new_name)
    elif choice == options[1]:
        pass


def time_conver(time_tex):
    '''convert time from h.m.s to sec'''
    value = re.findall("[0-9]+", time_tex)
    hour = int(value[0]) * 3600
    minute = int(value[1]) * 60
    second = int(value[2])
    suma = hour + minute + second
    return suma


def time_conver_from_secon(clip):
    '''convert time from sec to h.m.s'''
    # convert time from sec to h.m.s
    second = clip.duration
    # mins = (clip.duration % 3600) / 60
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    minute = str(int(minute))
    hour = str(int(hour))
    second = str(int(second))

    print("Duration : " + hour + "." + minute + "." + second)
    # convert back to seconds
    print("\nInput begining and the end of file as: 0.0.0")
    print("Begining:")
    start = input()
    start = time_conver(start)
    stop = input("The end:\n")
    stop = time_conver(stop)
    return start, stop


def cropp_video(name, path):
    '''cropping video'''
    source_path = path + "/" + name
    options = ['Cut Video [only]: ', 'Cut Audio and convert to mp3']
    choice = enquiries.choose('Choose one of these options: ', options)
    # cut only video into video
    if choice == options[0]:
        clip = VideoFileClip(source_path)
        start, stop = time_conver_from_secon(clip)
        clip = VideoFileClip(source_path).subclip(start, stop)
        print(start, stop)
        # num = 0
        name = rename_file(name)
        print(name)
        source_path = path + "/" + name
        clip.write_videofile(name + ".mp4", bitrate="4000k",
                             threads=1, preset='ultrafast', codec='h264')
    # cut audio and video into only audio
    elif choice == options[1]:
        clip = AudioFileClip(source_path)
        start, stop = time_conver_from_secon(clip)
        clip = AudioFileClip(source_path).subclip(start, stop)
        print(start, stop)
        name = rename_file(name)
        print(name)
        source_path = path + "/" + str(name)
        clip.write_audiofile(name + ".mp3")

    input("\nPress any key to continue..")


def video_play(youtube):
    '''preview video'''

    # Get the highest resolution stream for video playback
    video_stream = youtube.streams.get_highest_resolution()

    # Get the direct URL of the video stream
    video_stream_url = video_stream.url

    # Play the video stream using mpv
    mpv_command = ['mpv', video_stream_url]
    subprocess.run(mpv_command)


if __name__ == "__main__":
    '''main loop'''
    assert ('linux' in sys.platform), "This code runs on Linux only."
    path = os.getcwd()

    options = ['Download File', 'Crop file', 'Close']
    while True:
        os.system('clear')
        choice = enquiries.choose('Choose one of these options: ', options)
        if choice == options[0]:
            # url = "https://www.youtube.com/watch?v=ql9-82oV2JE&list=RDYiIhiDjrAWc&index=2"
            url = input("Enter url of video:\n")
            url = str(url)
            try:
                youtube = YouTube(url, on_progress_callback=progress)

                filesize = get_video_info(youtube)
                # video_play(url)
                optionss = ['Download Video', 'Download only sound', 'Back']
                choice = enquiries.choose('Choose one of these options: ', optionss)
                print(choice)
                if choice == optionss[0]:
                    down_yt_vid(youtube, path, 0)
                elif choice == optionss[1]:
                    down_yt_vid(youtube, path, 1)
                elif choice == optionss[2]:
                    continue
            # pytube.exceptions.RegexMatchError:
            except exceptions.RegexMatchError:
                print('The Regex pattern did not return any matches for the video: {}'.format(url))
            except exceptions.ExtractError:
                print('An extraction error occurred for the video: {}'.format(url))
            except exceptions.VideoUnavailable:
                print('The following video is unavailable: {}'.format(url))
            input("\nPress any key to continue..")
        elif choice == options[1]:
            # list files in folder
            dirs = os.listdir(path)
            for file in dirs:
                if isfile(join(path, file)):
                    print(file)
            # type file name from an above list
            file = input("Enter file name from files above:\n")
            try:
                open(file)
                cropp_video(file, path)
            except IOError:
                input("\nCant find this file.\nPress any key to try again..")
        elif choice == options[2]:
            print("See you soon!")
            break
