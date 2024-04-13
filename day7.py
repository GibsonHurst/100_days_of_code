print("Are you a data analysis expert? ")
q1 = input("Have you used linear regression before? ")
if q1 == "yes":
	print("That is good")
	q2 = input("How about logistic regression? ")
	if q2 == "yes":
		print("You know your stuff!")
	else:
		print("Well, that one is pretty important")
else:
	print("I would recommend you try linear regression")
	q3 = input("One more question, have you used a t-test before? ")
	if q3 == "yes":
		print("That's good")
	else:
		print("You likely are not an expert")