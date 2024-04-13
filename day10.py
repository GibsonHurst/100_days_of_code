myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = (int(input("what percentage tip would you like to provide? "))/100) + 1
answer = (myBill*tip) / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)

