# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
lis1 = [ ]
N=int(input())
for a in range(N):
    reg=input()
    lis1.append(reg)
    if a==reg:
        print('False')
    else:
        print('True')
