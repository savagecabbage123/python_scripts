import random
import time
lives = 6
guesses = ''
secretsentence = "walking"
print("welcome to hangman!")
print('''
you will have 6 lives and if you lose all six lives he will die''')
start = input('''
are you ready y/n: ''')
if start == "y":
	print("lets begin!")
elif start == "n":
		quit()
while lives > 0:
	print("lives: %s" % lives)
	if lives == 6:
		print("""			 _________
			 	 |
			 	 |
				 |
				 |
				 |
				 |
				 |
			  _______|_______
				""")
	elif lives == 5:
		print("""			 _________
			 |	 |
			 |	 |
			 	 |
				 |
				 |
				 |
				 |
			  _______|_______
				""")
	elif lives == 4:
		print("""			 _________
			 |	 |
			 |	 |
			 __	 |
			|__|	 |
			         |
			         |
				 |
			  _______|_______
			  """)
	elif lives == 3:
		print("""			 _________
			 |	 |
			 |	 |
			 __	 |
			|__|	 |
			  |      |
			  |      |
				 |
			  _______|_______
			  """)
	elif lives == 2:
		print("""			 _________
			 |	 |
			 |	 |
			 __	 |
			|__|	 |
			 /|\     |
			  |      |
			         |
			  _______|_______
			  """)
	elif lives == 1:
		print("""			 _________
			 |	 |
			 |	 |
			 __	 |
			|__|	 |
			 /|\     |
			  |      |
			 / \     |
			  _______|_______
			  """)
	failed = 0
	for char in secretsentence:
		if char in guesses:
			print(char)
		else:
			print("_")
			failed += 1
	if failed == 0:
		print ('''
you won!''')
		break
	guess = input("guess a letter: ")
	guesses += guess
	if guess in secretsentence:
		print("correct")
	if guess not in secretsentence:
		lives -= 1
		print("wrong")
if (lives <= 0):
	print("""			 _________
			 |	 |
			 |	 |
			 __	 |
			|__|	 |
			 /|\     |
			  |      |
			 / \     |
		DEAD	  _______|_______
			  """)
	time.sleep(.5)
	print("you killed him. What a horrible guesser you are!")
	time.sleep(1.5)
	quit()