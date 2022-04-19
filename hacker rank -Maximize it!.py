test_case,divider=map(int,input().split())
ans=0
while test_case:
    data=list(map(int,input().split(' ')))
    ans+=max(data)**2
    print(max(data)**2)
    test_case-=1
    print(divider-1)
else:
    print(ans%divider)
# pending 