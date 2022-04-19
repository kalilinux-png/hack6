from decimal import *
n=int(input())
dic={}
for a in range(1,n+1):
    name,m1,m2,m3=input().split()
    m1=float(m1);m2=float(m2);m3=float(m3)
    dic[name]=[m1,m2,m3]

name2=input()
result=dic[name2]
print(Decimal(sum(result)/3).quantize(Decimal('.01')))

