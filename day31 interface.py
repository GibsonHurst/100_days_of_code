BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
YELLOW = "\033[1;33m"
END = "\033[0m"

print(f"{RED}={END}={BLUE}= {YELLOW}Music App {BLUE}={END}={RED}=")
print()
rg = "Radio Gaga"
print(f"{END}{rg: >15}")
q = "Queen"
print(f"{YELLOW}{q: >10}")
print()
print(f"{END}PREV")
n = "NEXT"
print(f"{GREEN}{n: >9}")
p = "PAUSE"
print(f"{CYAN}{p: >15}")