import re
list1=[]
N=int(input())
for a in range(N):
    M=input()
    list1.append(M)
    try:
        re.search(M,list1)
    except SyntaxError:
        pass
    except :
        print('False')

    
   
