test = input("What test did you take? ")
max = int(input("What was the maximum score possible on this test? "))
score = int(input("What score did you get on this test? "))

percent = round((score/max)*100)
letter = ""
type = ""

if percent < 50:
	letter = "U"
	type = "bad"
elif percent < 59:
	letter = "D"
	type = "bad"
elif percent < 69:
	letter = "C"
	type = "bad"
elif percent < 79:
	letter = "B"
	type = "good"
elif percent < 89:
	letter = "A"
	type = "good"
elif percent <= 100:
	letter = "A+"
	type = "good"
else:
	letter = "ERROR"
	type = "ERROR"

print("On the test", test, "you received", percent, "percent correct which is a", letter, "letter grade. This is a", type, "grade.")

