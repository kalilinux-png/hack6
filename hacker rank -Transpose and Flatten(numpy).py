import numpy
list1=[]
N,M=map(int,input().split())
for a in range(N):
    list1.append(list(map(int,input().split())))
##    result=numpy.flatten(arr)
list1=numpy.array(list1)
print(list1.transpose())
print(list1.flatten())
