# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
for a in range(N):
    string=input()
    if re.search(r'^hackerrank \w+',string): # start 
        print('1')
    
    elif re.search(r'\w hackerrank$',string): # end
        print('2')
    elif re.search(r'^hackerrank$',string): 
        print('0')
    else: 
        print('-1')
''' THIS QUESTION WAS REALLY VERY LOGICAL '''
''' THANKS TO LORD KRISHNA FOR THIS MOGIC OF
LOGIC '''
''' AFTER A LOT TIME I GOT IN THE FLOW
'''
