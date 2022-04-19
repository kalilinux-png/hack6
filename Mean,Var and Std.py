import numpy
R,C = map(int,input().split())
list1=[]
for a in range(R):
    list1.append(list(map(int,input().split())))
list2=numpy.array(list1)
print(numpy.mean(list2,axis=1))
print(numpy.var(list2,axis=0))
print(round(numpy.std(list2),11))

