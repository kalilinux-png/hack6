import re
import email.utils
reg=reg=re.compile(r'[^\W_\.]+[\w\.\-]+@{1}[a-zA-Z]+\.[a-zA-Z]{1,3}$')
## ami reg=re.compile(r'^[a-zA-z]?[\w\.\-]+@{1}[a-zA-Z]+\.[A-Za-z]+[a-zA-Z]{,3}$')

##reg=re.compile(r'[a-zA-z]*[1-9a-zA-Z\.\-_]+@{1}[a-zA-Z]+\.[A-Za-z]+[a-zA-Z]{0,3}$')
n = int(input())
for k  in range(n):
    name,add=input().split()
    add2=add[1:-1]
    if reg.match(add2):
        print(name,add)
