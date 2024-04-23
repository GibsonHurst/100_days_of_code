years = float(input("Input a number of years: "))

minute = 60
hour = 60
day = 24
year = 365

seconds = round(years * year * day * hour * minute)

print("There are", seconds, "in", years, "year(s)")