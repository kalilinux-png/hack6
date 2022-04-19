input()
arr=list(map(int,input().split()))
arr.sort()
set1=sorted(set(arr))

print(set1[-2])
