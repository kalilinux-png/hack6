# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque   
e=deque()
n=int(input())
for a in range(n):
    c=input().split()
    if c[0]=='append':
        e.append(int(c[1]))
    elif c[0]=='pop':
        e.pop()
    elif c[0]=="appendleft":
        e.appendleft(int(c[1]))
       
    elif c[0]=="popleft":
        e.popleft()
for ele in e:
    print(ele,end=' ')
        ''' THANK YOU MY BHAGWAN'''
        '''15/02/2021-14:25'''
        '''MONDAY DAY AFTER VALENTINE'''
        ''' TOMMOROW VASANT PANCHMI '''
