# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
for a in range(N):
    string=input()
    pattern=re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]$')
    ans=pattern.search(string)
    if ans != None:
        print('YES')
    else:
        print('NO')
''' this question was also very easy but i was making mistakes
that are made by a noob and it all means that i was not focused
'''
''' THANK YOU GOD FOR MAKING ME UNDERSTAND THIS
 AND FOR THIS UNIVERSE'''
