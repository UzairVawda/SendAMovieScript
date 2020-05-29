import sys
import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 

# Click the three dots in the upper right hand corner 
# Select help > About Google Chrome
# https://chromedriver.chromium.org/ Download the appropriate version and replace the path
# driver = webdriver.Chrome("YOUR GOOGLE CHROME DRIVER PATH")

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

# Select file from user and wait time between messages 
file = input('Name of script file:\n> ')
messageDelay = float(input('Delay between each message: '))

# Open file as script and for each line fiter the "'" and send them one by one 
# I had to filt the "'" becasue they were causing the script to quit or crash 
with open(file, 'r') as script:
	lines = script.readlines()
	for line in lines:
		line = line.replace("'", "")
		try:
			messageBox.send_keys(line)
			driver.find_element_by_class_name('_35EW6').click()
			time.sleep(messageDelay)
		except:
			print("Sorry, something went wrong.")

script.close()