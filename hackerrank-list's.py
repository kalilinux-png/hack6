def insert():
            l1=list(map(int,n1[1:3]))
            l2.insert(l1[0],l1[1])
            
def prints():
    print(l2)
def removes():
    l1=list(map(int,n1[1:3]))
    l2.remove(l1[0])
    
##    l2.remove
def appends():
    l1=list(map(int,n1[1:3]))
    l2.append( l1[0])
    
def sorts():
    l2.sort()
def pops():
    l2.pop()
    
def reverses():
    l2.reverse()
    
if __name__=='__main__':
    n0=int(input())
    l2=[]
    for i in range(n0):
        n1=input().split()
        if n1[0]=='insert':
            insert()
        elif n1[0]=='print':
            prints()
        elif n1[0]=='remove':
            removes()
        elif n1[0]=='append':
            appends()
        elif n1[0]=='sort':
            sorts()
        elif n1[0]=='pop':
            pops()
        elif n1[0]=='reverse':
            reverses()
        

    
