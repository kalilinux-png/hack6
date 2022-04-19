import numpy
list1=[]
R,C = map(int,input().split())
for a in range(R):
    list1.append(list(map(int,input().split())))
array1=numpy.array(list1)
print(numpy.max(numpy.min(array1,axis=1)))

