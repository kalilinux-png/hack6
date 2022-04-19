import numpy
arr=[]
R,C = map(int,input().split())
for a in range(C):
    arr.append(list(map(int,input().split())))
arrae=numpy.array(arr)
sumit=numpy.sum(arrae,axis=0)
print(numpy.prod(sumit))
