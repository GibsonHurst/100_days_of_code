import random

pick = random.randint(1, 1000000)
count = 0

while True:
	num = int(input("Pick a number between 0 and 1,000,000: "))
	count += 1
	if num < 0 or num > 1000000:
		print("Invalid Number")
		continue
	if num < pick:
		print("Your pick is too low")
		continue
	elif num > pick:
		print("Your pick is too high")
		continue
	else:
		print("You pick is correct and it took", count, "tries.")
		exit()