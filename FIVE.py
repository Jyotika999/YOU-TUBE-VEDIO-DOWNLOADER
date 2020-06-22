# in this tutorial , we will be learning to download  a group of you tube vedios together in a single shot
from pytube import YouTube

listing = ["https://www.youtube.com/watch?v=nhtREXZgfP8","https://www.youtube.com/watch?v=UT58ETAj3cg" ]
# thinking of downloading the group of vedios , we basically make a list of links to the vedios and then within a for loop iterate through each of these vedios and then get them downloaded using object creation using 
for i in listing:
	yt = YouTube(i) # creating an object 
	dw = yt.streams.get_by_itag(22) #get the stream downloaded by itag 
	dw.download("Vedi/")