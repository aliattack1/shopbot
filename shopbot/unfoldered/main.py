# trying to simulate the behavior of a single user in telegram

import messagehandler
from user import User
while True:
	user_input = input("please input like a telegram user would plus the user id in the start:    ")
	if user_input == "quit()":
		quit()
	input_list = user_input.split(' ')
	id = input_list[0]
	user_message = user_input[len(id)+1:]
	
	messagehandler.handle(id, user_message)
	print(User.users)
	