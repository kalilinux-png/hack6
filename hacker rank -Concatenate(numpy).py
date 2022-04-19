import numpy
N,M,P=map(int,input().split())
arr=[]
arr2=[]
for a in range(N):
   a= list(map(int,input().split()))
   arr.append(a)
for c in range(M):
    b= list(map(int,input().split()))
    arr2.append(b)
print(numpy.concatenate((arr,arr2),axis=0))
'''this question was easy but i was not aware that's why it sucked a lot of time'''
# ----ENJOY CODEING----####
