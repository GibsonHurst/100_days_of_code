start = int(input("provide a starting number: "))
end = int(input("provide a number to end at: ")) + 1
increment = int(input("provide a number to increment by: "))

for i in range(start, end, increment):
	print(i)