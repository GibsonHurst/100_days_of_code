print("SECURE LOGIN")
print()
user = input("USERNAME: ")
password = input("PASSWORD: ")
print()
if user == "Gibson" and password == "12345":
	print("Welcome Gibson")
elif user == "Gibby" and password == "1234":
	print("Welcome Gibby")
elif user == "Gib" and password == "123":
	print("Weclome Gib")
else:
	print("Incorrect username or password!")