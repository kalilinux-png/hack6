n=int(input())
dict={}
for a in range(n):
    N,m1,m2,m3=input().split()
    m1=float(m1);m2=float(m2);m3=float(m3)
    dict[N]=([m1,m2,m3])
A=input()
if A in dict.keys():
    mark=round(sum(dict[A])/4)
    
    print(f'{mark}')
       
    
