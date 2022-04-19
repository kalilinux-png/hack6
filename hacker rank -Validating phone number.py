# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
import re
for a in range(n):
    number=input()
    phone_no=re.search(r'^[789]\d{9}',number)
    if phone_no:
        print('YES')
    else:
        print('NO')
