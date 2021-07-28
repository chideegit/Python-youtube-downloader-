# pip install pytube
from pytube import YouTube

link = input("Enter URL") # Enter the link of the youtube video here
video = YouTube(link)
stream = video.streams.get_highest_resolution()

stream.download() # you can specify for the path you want to download the video in