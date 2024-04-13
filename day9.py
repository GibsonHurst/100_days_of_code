print("Discover what generation you are apart of")
year = int(input("What year were you born? "))
if (year >= 1925) and (year <= 1946):
	print("Traditionalist")
elif (year >= 1947) and (year <= 1964):
	print("Baby Boomer")
elif (year >= 1965) and (year <= 1981):
	print("Gen X")
elif (year >= 1982) and (year <= 1995):
	print("Millenial")
elif (year >= 1996) and (year <= 2015):
	print("Gen Z")
else:
	print("IDK your generation")
