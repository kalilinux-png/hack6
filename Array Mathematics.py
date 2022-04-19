import numpy
arr1=[]
arr2=[]
N,M=map(int,input().split())
for a in range(N):
    arr1.append(list(map(int,input().split())))
for a in range(N):
    arr2.append(list(map(int,input().split())))
arr1=numpy.array(arr1)
arr2=numpy.array(arr2)
  
print(numpy.add(arr1,arr2))
print(numpy.subtract(arr1,arr2))
print(numpy.multiply(arr1,arr2))
print(arr1//arr2)
print(numpy.mod(arr1,arr2))
print(numpy.power(arr1,arr2))

### THANKS TO GOD FOR HELPING ME ###
''' THIS QUESTION FUCKED ME BUT I BOUNCED BACK
AND KICKED THE ASS OF THIS BUSTERD '''
''' ORIGNAL CODE
import numpy

N, M = map(int, raw_input().split())
A =  numpy.array([map(int, raw_input().split()) for i in range(N)])
B =  numpy.array([map(int, raw_input().split()) for i in range(N)])

print A + B
print A - B
print A * B
print A / B
print A % B
print A ** B
'''
