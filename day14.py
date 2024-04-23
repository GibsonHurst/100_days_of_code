from getpass import getpass as input
print("Welcome to Rock Paper Scissors")
player1 = input("Player 1, what is your move? (R, P, S) ")
player2 = input("Player 2, what is your move? (R, P, S) ")

if player1 == player2:
	print("DRAW")
elif player1 == "R":
	if player2 == "P":
		print("Player 2 Wins")
	else:
		print("Player 1 Wins")
elif player1 == "P":
	if player2 == "S":
		print("Player 2 wins")
	else:
		print("Player 1 wins")
else:
	if player2 == "R":
		print("Player 2 wins")
	else:
		print("Player 1 wins")