import re
n=int(input())
for i in range(n):
    num=input()
    if re.match('[789]\d{9}$', num):
        print("YES")
    else:
        print("NO")