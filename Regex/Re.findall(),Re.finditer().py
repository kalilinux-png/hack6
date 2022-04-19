import re
string=input()
ans=re.compile(r'(?<=[QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm])')
ans1=ans.findall(string)
if ans1:
    print(*ans1,sep='\n')
else:
    print('-1')
    ''' this is question is just done ans i wanna thanks lord krishna
for this help and awesomeness and for the target '''
