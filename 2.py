import re
s=input()
print(*re.split("[,.]", s), sep="\n")