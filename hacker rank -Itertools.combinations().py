from itertools import combinations
a,b=input().split();b=int(b)
c=sorted(set(combinations(a,b)))
for i in c:
    print(i,sep="")
