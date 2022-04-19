from itertools import product
def give():
    n1=list(map(int,input().split()))
    n2=list(map(int,input().split()))
    n3=list(product(n1,n2))
    for i in n3 :
        print(i,sep=",",end=" ")
give()
