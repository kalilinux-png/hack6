# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
for a in range(N):
    username=input()
    pattern=re.compile(r'^[ _\.][0-9]+[a-zA-Z]*_?$')
    ans=pattern.search(username)
    if ans == None:
        print('INVALID')
    else:
        print('VALID')
''' this question was also solved in shocking way
after all its all my bhagwan kripa or blessing's or love
time: 10-32
date:21-02-2021
'''
''' a very big thanks to you my bhagwan for all this awesome
things and the awesome universe '''
