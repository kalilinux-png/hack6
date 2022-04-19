laist=[]
Test_case=int(input())
for a in range(1,Test_case+1):
    input()
    set_no1=set(map(int,input().split()))
    input()
    set_no2=set(map(int,input().split()))
    if  set_no1.issubset(set_no2):
        laist.append('True')
    else:
        laist.append('False')
for a in laist:
    print(a)
