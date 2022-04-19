n=int(input())
MONEY=0
size=list(map(int,input().split()))
No_chance=int(input())
for a in range(No_chance):
    S,M=map(int,input().split())
    if S in size:
        size.remove(S)
        MONEY+=M
print(MONEY)
        
''' CONCEPT '''
'''
>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
'''
