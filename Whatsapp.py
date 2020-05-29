import sys
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

#driver = webdriver.Chrome("LOCATION OF GOOGLE CHROME DRIVER")
driver = webdriver.Chrome("/Users/UzairVawda/Sites/ScriptSending/driver/chromedriver")
driver.get("http://web.whatsapp.com")
wait = WebDriverWait(driver, 600) 

input("Enter anything after scanning QR code in your web browser!")

userChoice = (input("Enter Recipents Username or Groupchat Name:\n> "))
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(userChoice))
user.click()

messageBox = driver.find_element_by_class_name('_1Plpp')


file = input('Name of script file:\n> ')
messageDelay = float(input('Delay between each message: '))

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