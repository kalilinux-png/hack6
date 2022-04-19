import math
n=int(input())
pair=[]
arr=list(map(int,input().split()))
print(arr)
arr_set=set(arr)
for a in arr_set:
    mo=arr.count(a)/2
    mo=math.floor(mo)
    pair.append(mo)
print(sum(pair))
