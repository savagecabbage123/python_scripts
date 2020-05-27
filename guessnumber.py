import random
print("I am thinking of a number between 1 and 100.")
random_number = random.randrange(1,100)
tries = 1
guess = ()
while guess != random_number:
	guess = int(input("what do you think that number is?:"))
	print(guess)
	if guess > random_number:
		print("too high")
		tries += 1
	elif guess < random_number:
		print("too low")
		tries += 1
	elif guess == random_number:
		print("you guessed it right!")
		print("it took you %d tries to get it right" % tries)