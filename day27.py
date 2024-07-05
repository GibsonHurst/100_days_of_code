import random
import time
import os

def roll(sides):
	return random.randint(1,sides)

def health_points():
	return ((roll(6)*roll(12))/2) + 10

def strength_points():
	return ((roll(6)*roll(12))/2) + 12

keepGoing = "y"
print("Character Builder")
print()

while keepGoing == "y":
	name = input("What is your character name? ")
	type = input("What is your character type? (human, wizard, or elf) ")
	health = health_points()
	strength = strength_points()
	print()
	print(name + " the " + type)
	print("HEALTH: " + str(health))
	print("STRENGTH: " + str(strength))
	print()
	keepGoing = input("Build another character? (y/n)")
	if keepGoing == "y":
		os.system("clear")
	