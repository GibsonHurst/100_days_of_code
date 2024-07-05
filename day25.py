def rollDice(sides):
  import random
  roll = random.randint(1,sides)
  return roll

def hp():
  hp = rollDice(6) * rollDice(8)
  return hp

play = "Y"

print("Character Stats Generator")
while play == "Y":
  print()
  name = input("Name your worrior: ")
  print(name + " has " + str(hp()) + "hp.")
  play = input("Play again? (Y/N)")
  if play == "N":
    print()
    print("Thanks for playing")