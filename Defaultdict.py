from collections import defaultdict
d=defaultdict(list)
list2=[]
A,B=map(int,input().split())
for a in range(1,A+1):
    d[input()].append(a)
    
for a in range(1,B+1):
##    list2.append(input())
    n=input()
    if n in d.keys():
        for k in d[n]:
            print(k,end=' ')
        print(' ') #IN this i got the task prove myself
    else:
        print('-1')
