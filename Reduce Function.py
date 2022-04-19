from fractions import Fraction
list1=[]
for a in range(int(input())):
    list1.append(Fraction(*map(int,input().split())))
reduce(lambda x,y:x*y,list1)
