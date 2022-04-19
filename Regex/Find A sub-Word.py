import re
list1=[]
N=int(input())
for a in range(N):
    list1.append(input())
string=' '.join(list1)
subin=int(input())
for c in range(subin):
    subword=input()
    find=re.compile(f'\w{subword}\w')
    ans=find.findall(string)
    print(len(ans))
''' I SAW THE SOLUTION OF THIS THE MAIN PROBLEM WAS
WITH THE REGEX AND ALL WAS GOOD
SO I GOT 0 POINTS FOR THIS '''
''' THANKS BHAGWAN FOR GIVING ME NEW CONCEPT IN THIS
QUESTION AND FOR THIS UNIVERSE '''
