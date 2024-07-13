total = 0
print("30 Days Down!")
for i in range(1,31):
	print()
	print(f"Day {i}")
	rating = int(input("Rate this lesson on a scale of 1 to 10 "))
	print(f"You thought lesson {i} was a {rating}.")
	total += rating

average = round(total/30)
print(f"Thank you for your feedback. Your average score was {average}.")
	