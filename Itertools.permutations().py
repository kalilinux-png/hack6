from itertools import permutations
a,b=input().split();b=int(b)
c=sorted(set(permutations(a,b)))
for i in c:
    print(i,sep="  ")
