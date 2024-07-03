def rollDice(sides):
	import random
	roll = random.randint(1,sides)
	print("You rolled: ", roll)

print("Dice with any number of sides")
sides = int(input("How many sides on your dice? "))
rolls = int(input("How many times would you like to roll? "))

for i in range(rolls):
	rollDice(sides)