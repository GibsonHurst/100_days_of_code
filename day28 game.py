import random
import time
import os

def roll(sides):
	return random.randint(1,sides)

def health_points():
	return ((roll(6)*roll(12))/2) + 10

def strength_points():
	return ((roll(6)*roll(12))/2) + 12

print("Character Builder")
print()
name1 = input("What is character 1's name? ")
type1 = input("What is character 1's type? (human, wizard, or elf) ")
health1 = health_points()
strength1 = strength_points()
print()
name2 = input("What is character 2's name? ")
type2 = input("What is character 2's type? (human, wizard, or elf) ")
health2 = health_points()
strength2 = strength_points()
print()
print(name1 + " the " + type1)
print("HEALTH: " + str(health1))
print("STRENGTH: " + str(strength1))
print()
print(name2 + " the " + type2)
print("HEALTH: " + str(health2))
print("STRENGTH: " + str(strength2))

round = 1
time.sleep(3)

while (health1 > 0) & (health2 > 0):
	time.sleep(1)
	os.system("clear")
	
	print("Round: ", str(round))
	round += 1

	time.sleep(3)
	coin = roll(2)
	if coin == 1:
		print(name1, "won the round")
		health2 = health2 - (abs(strength2 - strength1) + 1)
	else:
		print(name2, "won the round")
		health1 = health1 - (abs(strength2 - strength1) + 1)

	time.sleep(1)
	print(name1, "HEALTH =", health1)
	print(name2, "HEALTH =", health2)

if health1 < health2:
	winner = name2
	loser = name1
else:
	winner = name1
	loser = name2
	
os.system("clear")
print("Oh no, " + loser + " has died. " + winner + " wins the battle in round " + str(round) + ".")


		
	
