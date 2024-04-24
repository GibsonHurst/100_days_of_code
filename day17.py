from getpass import getpass as input
print("Welcome to Rock Paper Scissors")
p1score = 0
p2score = 0

while True:
		if p1score == 3 or p2score == 3:
				exit()
		else:
				player1 = input("Player 1, what is your move? (R, P, S) ")
				player2 = input("Player 2, what is your move? (R, P, S) ")

				if player1 == player2:
						print("DRAW")
				elif player1 == "R":
						if player2 == "P":
								print("Player 2 Wins")
								p2score += 1
								continue
						else:
								print("Player 1 Wins")
								p1score += 1
								continue
				elif player1 == "P":
						if player2 == "S":
								print("Player 2 wins")
								p2score += 1
								continue
						else:
								print("Player 1 wins")
								p1score += 1
								continue
				else:
						if player2 == "R":
								print("Player 2 wins")
								p2score += 1
								continue
						else:
								print("Player 1 wins")
								p1score += 1
								continue

if p1score == 3:
		print("Player 1 Wins Best Out of Three")
else:
		print("Player 2 Wins Best Out of Three")
