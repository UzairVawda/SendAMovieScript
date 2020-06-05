# import os for osascript, import sys to exit, import time for delay, import lyricsgenius for song lyrics
import os
import sys
import time 
import lyricsgenius

# enter recipents phone number, iniitialize genius
number = input("Enter Recipents Phone Number:\n(Do Not include dashes or parenthesies. Just the 10 digit number):\n> ")
genius = lyricsgenius.Genius("hsirmoWcQW6Xize7OXuF2WjUZcQqHCpwgksh7uLm-xUL_b5hd3oJ33wOq0SmIX3M")

# specify song and message delay
specificSong = str(input("What song would you like to search for?\n> "))
messageDelay = int(input("Delay between each messages in seconds:\n> "))

# search genius for the song
song = genius.search_song(specificSong)

# check if song exisits
if (song == None):
	print ("Could not find", specificSong)
	sys.exit()

# split song by new line
songLyrics = song.lyrics
songLyrics = songLyrics.split("\n")

print ("Sending lyrics to " + number + "...")

# send song line by line
for line in songLyrics:
	line = line.replace("'", "")
	os.system("osascript sendMessages.scpt %s '%s'" %(number, line))
	time.sleep(messageDelay)

print ("Done sending lyrics!")
