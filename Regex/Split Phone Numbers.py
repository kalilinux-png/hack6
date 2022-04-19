# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
N=int(input())
for a in range(N):
    mobile_no=input()
    pattern=re.compile(r'^([0-9]+)[\s-]([0-9]+)[\s-]([0-9]+)$')
    Ans=pattern.search(mobile_no)
    print(f'CountryCode={Ans.group(1)},LocalAreaCode={Ans.group(2)},Number={Ans.group(3)}')
   ''' this question taught me a lot of things that include  grouping
importance  and the importance of + it is actually really helpful
'''
''' HEY BHAGWAN AHAM TUWAM DHANYWAADAM KARAKSHAME'''
''' BHAGWAN THANKS A LOT FOR THIS CONCEPT ANS
THE AWESOME UNIVERSE'S '''
''' AND FOR THIS BEAUTIFUL VEENA MUSIC '''
''' AND FOR THE MADRASHTKAM BY AGAM '''
''' AND FOR EVERYTHING I GOT '''
