def colorPrint(color, words):
  if color == "red":
    RED = "\033[0;31m"
    print(RED, words, sep="")
  elif color == "blue":
    BLUE = "\033[0;34m"
    print(BLUE, words, sep="")
  elif color == "green":
    GREEN = "\033[0;32m"
    print(GREEN, words, sep="")
  else:
    print("Unknown color: ", words, sep="")
    
color = input("Pick a color: ")
words = input("Write your message: ")

colorPrint(color, words)