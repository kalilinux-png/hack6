import re

def repa(match):
    match=match.group(0)
    if match==' && ':
        match=' and '
    else :
        match=' or '
    return match
if __name__=='__main__':
    n=int(input())
    data=[ ]
    for k in range(n):
        data.append(input()+'\n')
        
    data=''.join(data)
    ans1=re.sub(r' && | \|\| ',repa,data)
    ans2=re.sub(r' && | \|\| ',repa,ans1)
    print(ans2)

# more easy sol is available but it is cheap but good 
