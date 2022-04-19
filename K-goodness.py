# global or local score
def goodness(string):
    score=0
    if len(string)%2==1:
        upto=(len(string)//2)+1
    else:
        upto=len(string)//2
    for a in range(2,upto+1):
        check=len(string)-a+1
        print(a,string[a],check,string[check])
        if string[a]!=string[check]:
            score+=1
        print(score)
T=int(input())
for i in range(T):
    lenght,ans=map(int,input().split())
    goodness(input())
    
    

