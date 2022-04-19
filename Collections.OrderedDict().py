from collections import OrderedDict
T=int(input())
items=OrderedDict()
for a in range(T):
    *a,b=input().split();b=int(b)
    a=' '.join(a)
    if a in items:
        items[a]=items.get(a)+b
    else:
        items[a]=b
for c,d in items.items():
    print(c,d)
