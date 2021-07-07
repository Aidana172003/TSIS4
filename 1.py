import re
n=int(input())
for i in range(n):
    num=input()
    print(bool(re.match('^[-+]?\d*\.\d+$', num)))