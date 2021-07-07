import re
s=input()
print(*re.findall('[AEIOUaeiou]{2,}', s) ,sep="\n")