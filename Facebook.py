import sys
import time
import fbchat
import getpass
from fbchat.models import *

client = fbchat.Client(input('Your username:\n> '), getpass.getpass())
user_choice = (input('Do you want to spam a user or a groupchat?\n1)User\n2)Groupchat\n> ')).lower()

while user_choice not in ['1', '2', 'user', 'groupchat']:
	user_choice = input('Please enter valid answer (user/groupchat)\n> ').lower()

if user_choice == 'user' or user_choice == '1':
	friends = client.searchForUsers(input('Who do you want to spam?\n> '))
	thread_id = friends[0].uid
	thread_type = ThreadType.USER
elif user_choice == 'groupchat' or user_choice == '2':
	groups = client.searchForGroups(input('Which group do you want to spam?\n> '))
	thread_id = groups[0].uid
	thread_type = ThreadType.GROUP
else:
	print ("I don't know how you got here.")
	sys.exit(0)

file = input('Name of script file:\n> ')
messageDelay = float(input('Delay between each message: '))

with open(file, 'r') as script:
	lines = script.readlines()
	for line in lines:
		line = line.replace("'", "")
		try:
			client.send(Message(text=line), thread_id=thread_id, thread_type=thread_type)
			time.sleep(messageDelay)
		except:
			print("Sorry, we've reached Facebook's spam limit.")

script.close()