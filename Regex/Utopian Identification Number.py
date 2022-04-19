import re
N=int(input())
for a in range(N):
    string=input()
    pattern=re.compile(r'^[a-z]{0,3}[\d]{2,8}[A-Z]{3,}$')
    ans=pattern.search(string)
    if ans:
        print('VALID')
    else:
        print('INVALID')

''' something weird happening out here this code is working but
the code below is not working and they are same '''
'''THANK YOU BHAGWAN FOR THIS UNIVERSE AND FOR THIS
ALL '''






















##
##
##
##import re
##N=int(input())
##for a in range(N):
##    string=input()
##    pattern=re.compile(r'^[a-z]{0,3}[\d]{2,8}[A-Z]{3,}$')
####    pattern=re.compile(r'^[a-z]{0,3}[\d]{2,8}[A-Z]{3,}$ ') 
##    ans=pattern.search(string)
##    print(ans)
##    if ans:
##        print('VALID')
##    else:
##        print('INVALID')
##''' test cases 1:abc012333ABCDEEEE=ans==valid
##test cases 2:0123AB=ans==invalid'''
####
##
