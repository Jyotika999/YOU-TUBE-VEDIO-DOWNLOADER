# In this tutorial , we will learn how to download 2-3 vedios in a single shot , using a listt of vedio url's stored in a text file 

from pytube import YouTube

listing = open("sets.txt", "r")

for i in listing:
	yt = 		YouTube(i)
	dw = yt.streams.get_by_itag(22)
	dw.download("VVV/")
	print("doenloaded", i)