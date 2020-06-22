# a program to get all the imformation of youtube vedio using pytube 

# IMporting YouTube module from Pytube library
from pytube import YouTube

# now , we are basically promoting the user for a YouTube vedio Link 

yt = input("PLEASE ENTER A YOU TUBE LINK:  ")

#Now, we are creating a YouTube object with the link 

obj = YouTube(yt)

print("THE TITLE OF THE VIDEO IS :" + obj.title) # this will print the title of the youtube vedio
