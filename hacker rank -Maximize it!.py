test_case,divider=map(int,input().split())
ans=0
while test_case:
    try:
        data=list(map(int,input().split(' ')))
    except:
        pass
    largest=max(data)
    tempo =largest**2
    print(largest)
    if tempo>divider:
        print('remvove',largest)
        data.remove(largest)
        continue
    print("largest found",largest)
    ans+=tempo
    test_case-=1
    
print(ans%divider)
