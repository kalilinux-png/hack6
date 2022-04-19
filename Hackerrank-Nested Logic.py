d1,m1,y1=input().split()
d1=int(d1);m1=int(m1);y1=int(y1)
d2,m2,y2=input().split()
d2=int(d2);m2=int(m2);y2=int(y2)
D1= int(d1-d2)
M1= int(m1-m2)
Y1= int(y1-y2)
if Y1>0:
    print(Y1*10000)
if D1>0:
    print(D1*15)
    if  M1>0:
        print(M1*500)
else :
    print('0')


        
