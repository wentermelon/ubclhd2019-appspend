USER_DATA_ADDRESS = 'UserData.txt'

def readUserData(address):
	f = open(address, 'r')
	data = f.readlines()
	splittedData = []
	for string in data:
		splittedData.append(string.split())
	return splittedData

def login(address, name, password):
	data = readUserData(address)
	for user in data:
		if user[0] == name:
			if user[1] == password:
				return True

def signUpToFile(address, name, password):
	data = readUserData(address)
	for user in data:
		if user[0] == name:
				return False
	# if not exist, write to file
	f = open(address, 'a')
	f.write(name + ' ' + password + '\n')
	f.close()
	return True

def signUp():
	while True:
		userName = raw_input("YOU ARE SIGNING UP! Enter your name: ")
		password = raw_input('Enter your password: ')
		if signUpToFile(USER_DATA_ADDRESS, userName, password):
			print('Successfully signing up!')
			return
		else:
			print('Username already exists! Please try again')

def signIn():
	while True:
		userName = raw_input("YOU ARE SIGNING IN! Enter your name: ")
		password = raw_input('Enter your password: ')
		if login(USER_DATA_ADDRESS, userName, password):
			print('Successfully logging in!')
			return True
		else:
			print('Login fail, please try again!')












 