input()
arr=list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))


happy=[]
def fun():
    for i in arr:
        if i in A:
            happy.append(1)
            
        if i in B:
            happy.append(-1)
    return sum(happy)
print(fun())
