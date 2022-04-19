n,m =input().split()
n=int(n);m=int(m)
def draw():
    for i in range(1,(n-2)+1,2):
        print(('.|.'*i).center(m,'-'))
    print("WELCOME".center(m,'-'))
    for a in range(n-2,0,-2):
         print(('.|.'*a).center(m,'-'))

draw()
