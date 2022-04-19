# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
for a in range(N):
    string=input()
    pattern=re.compile(r'^[hH][iI][\s]+[^dD]')
    ans=pattern.search(string)
    if ans != None:
        print(string)

''' this question was done by god krishna and thank you very much god
for helping me out
'''
''' i was took a nap for 5 min and when i woked up the question
was solved and when i sumited it it passed all the test cases '''
