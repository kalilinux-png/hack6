from collections import namedtuple
marks=0
Data=namedtuple('data',input().split())

for a in range(int(input())):
    L.append(Data(*input().split()))
    marks+=int(Data(*input().split()).MARKS)
print(marks/T)
''' in 4 lines'''
