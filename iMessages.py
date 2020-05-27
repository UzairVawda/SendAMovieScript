import os

count = int(input("How many people would you like to spam?\n> ")) 

if count == 1: 
	userNumber = input("Enter Recipients Phone Number:\n> ")
	file = str(input("File Name:\n>"))

	with open(file, 'r') as script:
		lines = script.readlines()
		for line in lines:
			line = line.replace("'", "")
			os.system("osascript sendMessagesUser.scpt %s '%s'" %(userNumber, line))

	script.close()

elif count > 1:
	groupNumber = input("Enter Recipients Phone Number Seperated By A Comma:\n> ")
	print (groupNumber)
	groupNumber = groupNumber.split(",")
	print (groupNumber)
	# file = str(input("File Name:\n>"))

	# with open(file, 'r') as script:
	# 	lines = script.readlines()
	# 	for line in lines:
	# 		line = line.replace("'", "")
	# 		os.system("osascript sendMessagesUser.scpt %s '%s'" %(groupNumber, line))