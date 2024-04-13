name = input("Name: ")
if name == "Gibson" or name == "gibson":
	print("Hi Gibson")
	day = input("What day of the week is it? ")
	color = input("What is your favorite color? ")
	number = input("Pick a number from 1 to 7: ")
	prediction = ("you will see ", number, "things that are", color)
	if day == "Monday":
		print("This Monday, you will see", number, "things that are", color)
	elif day == "Tuesday":
		print("This Tuesday, you will see", number, "things that are", color)
	elif day == "Wednesday":
		print("This Wednesday, you will see", number, "things that are", color)
	elif day == "Thursday":
		print("This Thursday, you will see", number, "things that are", color)
	elif day == "Friday":
		print("This Friday, you will see", number, "things that are", color)
	elif day == "Saturday":
		print("This Saturday, you will see", number, "things that are", color)
	else:
		print("This Sunday, you will see", number, "things that are", color)
else:
	print("I don't know you")