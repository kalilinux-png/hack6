A=set(map(int,input().split()))
list1=[]
n=int(input())
for a in range(n):
    m=set(map(int,input().split()))
    ans=m.issuperset(A)
    list1.append(ans)
for a in list1:
     print(a)
##     if a=='False':
##         Ans="False"
##     else:
##         Ans='True'


         
##print(Ans)
        
