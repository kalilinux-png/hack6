from cgi import print_directory


def recursive(level,score):
    if level==6:
        return score

def hour(level1,level2,sum):
    global array
    for k in range(level2,level2+3):
        sum+=array[level1][k]
    sum+=array[level1+1][level2+1]
    for k in range(level2,level2+3):
        sum+=array[level1+2][k]
    return sum
array=[ ]
for k in range(6):
    temp=list(map(int,input().split(' ')))
    array.append(temp)

total=hour(0,0,0)

for k in range(4):
    for level2 in range(4):
        temp=hour(level2,k,0)
        print(temp)
        if  temp>total:
            total=temp

print(total)