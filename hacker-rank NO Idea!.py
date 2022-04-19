input()
arr=tuple(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
happy=0




for i in arr:
    if i in A:
        happy+=1
    if i in B:
        happy-=1
print(happy)
''' it worked in surprising way small changes makes a big chages '''
''' THANK  YOU VERY MUCH MY BHAGWAN  '''
'''
TIPS: TUPLE ARE FASTER THAN LIST
'''
