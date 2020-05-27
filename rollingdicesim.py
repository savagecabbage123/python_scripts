import random
while True:
	print("would you like to roll a die?")
	user_input = input("y/n?")
	if user_input == ("y"):
		roll = random.randrange(1,7)
		print(roll)
	elif user_input == ("n"):
		print("ok, bye")
		quit()
	