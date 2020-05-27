import os

number = input("Enter Phone Number:\n>")
file = str(input("File Name:\n>"))

with open(file, 'r') as script:
	lines = script.readlines()
	for line in lines:
		line = line.replace("'", "")
		os.system("osascript sendMessages.scpt %s '%s'" %(number, line))

script.close()

