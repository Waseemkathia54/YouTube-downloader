from pytube.cli import on_progress
from pytube import YouTube
import os

url = input("Drop YouTube Link \n")

try:
	youtube = YouTube(url,on_progress_callback=on_progress)
	youtube.streams\
	     .filter(file_extension='mp4')\
	     .get_highest_resolution()\
	     .download(/sdcard)
except EOFError as err:
	print(err)
	
else:
	print("Downloading Complete \n")
