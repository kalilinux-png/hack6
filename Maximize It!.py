##import math
##M,N= map(int,input().split())
##def square(n):
##    return n*n
##def max_int(M):
##    for a in range(M):
##        yield max(map(int,input().split()))
##
####print(sum(list(map(square,list(max_int(M)))))%N)
M,N= map(int,input().split())
list1= []
for a in range(M):
    list1.append(max(map(int,input().split())))
    print(list1)
print(sum(tuple([ a*a for a in list1]))%N)
    
