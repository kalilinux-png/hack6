import re
N=int(input())
for c in range(N):
    a=input()
    ma=re.search('^[+-.0-9][.0-9][0-9]+',a)
    print(ma)
    if ma:
        print('True')
    else:
        print('False')
