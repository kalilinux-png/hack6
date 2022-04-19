# compare the triplets

a1,a2,a3=map(int,input().split())
b1,b2,b3=map(int,input().split())
alice=[]
bob=[]
if a1>b1  :
    alice.append(1)
if  a2>b2  :
    alice.append(1)
if  a3>b3 :
    alice.append(1)
if a1<b1 :
    bob.append(1)
if  a2<b2:
    bob.append(1)
if a3<b3:
    bob.append(1)
else:
    alice.append(0)
    bob.append(0)
print(sum(alice),sum(bob))
