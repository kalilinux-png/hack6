n=int(input())
for a in range(n):
        try:
            a,b=map(int,input().split())
            print(a//b)
        except Exception as e:
            print('Error code:',e)
        
        
