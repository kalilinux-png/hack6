import doctest
from itertools import permutations
a,b=input().split();b=int(b)
c=sorted(set(permutations(a,b)))
for i,d in c:
    if d in c:
        print(i,d,sep="")
    else:
        print(i,sep='')
docktest.testmod()
