n=int(input())
##steps=0
clouds = tuple(map(int,input().split()))
##for a in range(len(clouds)):
##    if clouds[a+2]==0:
##        print('jump +2')
##        steps+=1
##        print(steps)
##        continue
##    elif clouds[a+1]==0:
##        print('jumps +1')
##        steps+=1
##        print(steps)
##        continue
##    else:
##        print('NONE')
##
steps= 0
size=0
try:
    while size<=len(clouds)+1:
        if clouds[size+2]==0:
            size+=2
            steps+=1
            print(f'size {size} ,steps {steps}')
        elif clouds[size+1]==0:
            size+=1
            steps+=1
            print(f'size {size} ,steps {steps}')
        else:
            print('NONE')
except IndexError:
    pass
print(steps)
print(f'finnal size {size} ,steps {steps}')
