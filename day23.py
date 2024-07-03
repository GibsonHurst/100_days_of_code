correct_username = "gibson"
correct_password = "1234"

def login():
	control = True
	while control:
		username = input('Username: ')
		password = input('Password: ')

		if (username == correct_username) & (password == correct_password):
			print("Welcome")
			control = False
		elif username != correct_username:
			print("Incorrect Username or Password")
			print()
		else:
			print("Incorrect Password")
			print()


print("Login system")
login()
print()