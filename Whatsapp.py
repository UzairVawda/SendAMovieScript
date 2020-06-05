# import sys to exit, import lyricsgenius for song lyrics, import time for delay
# import webdriver to get chrome and import WebDriverWait for time delay while opening
import sys
import lyricsgenius
import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 

# Click the three dots in the upper right hand corner 
# Select help > About Google Chrome
# https://chromedriver.chromium.org/ Download the appropriate version and replace the path
# driver = webdriver.Chrome("YOUR GOOGLE CHROME DRIVER PATH")
genius = lyricsgenius.Genius("hsirmoWcQW6Xize7OXuF2WjUZcQqHCpwgksh7uLm-xUL_b5hd3oJ33wOq0SmIX3M")
driver = webdriver.Chrome("/Users/UzairVawda/Sites/ScriptSending/driver/chromedriver")

# Load whatsapp in the chrome beowser and wait 
driver.get("http://web.whatsapp.com")
wait = WebDriverWait(driver, 1000) 

# Check if the user scanned the QR Code
input("Enter anything after scanning QR code in your web browser! (WAIT FOR THE BROWSER TO FULLY LOAD!)")

# Get the input from the users 
userChoice = (input("Enter Recipents Username or Groupchat Name: (THIS IS CASE AND EMOJI SENSITIVE)\n> "))

# Select the user tile with the user and then click it
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(userChoice))
user.click()

# Select the message box 
messageBox = driver.find_element_by_class_name('_1Plpp')

# Select song to send and wait time between messages
specificSong = str(input("What song would you like to search for?\n> ")) 
messageDelay = int(input('Delay between each messages in seconds: '))

song = genius.search_song(specificSong)

if (song == None):
	print ("Could not find", specificSong)
	sys.exit()

songLyrics = song.lyrics
songLyrics = songLyrics.split("\n")

print ("Sending lyrics to " + userChoice + "...")

# send song line by line
for line in songLyrics:
	messageBox.send_keys(line)
	driver.find_element_by_class_name('_35EW6').click()
	time.sleep(messageDelay)

print ("Done sending lyrics!")
