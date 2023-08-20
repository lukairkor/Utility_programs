import subprocess
import pytube

# Replace 'video_url' with the URL of the YouTube video you want to play
video_url = "https://www.youtube.com/watch?v=ql9-82oV2JE&list=RDYiIhiDjrAWc&index=2"

def play_youtube_video(video_url):
    # Create a YouTube object
    youtube = pytube.YouTube(video_url)

    # Get the highest resolution stream for video playback
    video_stream = youtube.streams.get_highest_resolution()

    # Get the direct URL of the video stream
    video_stream_url = video_stream.url

    # Play the video stream using mpv
    mpv_command = ['mpv', video_stream_url]
    subprocess.run(mpv_command)

play_youtube_video(video_url)
