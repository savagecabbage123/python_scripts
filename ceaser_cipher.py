print("welcome to caesar cipher")
maxKeySize = 26

def getMode():
	while True:
		print("do you want to decrypt or encrypt or brute force a message?")
		mode = input().lower()
		if mode in "encrypt e decrypt d brute b".split():
			return mode
		else:
			print ("enter either e, encrypt, d, decrypt, or brute b to continue.")
			
def getMessage():
	print("enter your message: ")
	return input()
	
def getKey():
	key = 0
	while True:
		print("enter the key number (1-%s)" % (maxKeySize))
		key = int(input())
		if (key >= 1 and key <= maxKeySize):
			return key

def getTranslatedMessage(mode, message, key):
	if mode[0] == 'd':
		key = -key
	translated = ''
	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key
			if symbol.isupper():
                                if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
					
			translated += chr(num)
		else:
			translated += symbol
	return translated

mode = getMode()
message = getMessage()
if mode[0] != 'b':
	key = getKey()

print("your translated text is: ")
if mode[0] != 'b':
	print(getTranslatedMessage(mode, message, key))
else:
	for key in range(1, maxKeySize + 1):
		print(key, getTranslatedMessage('decrypt', message, key))
