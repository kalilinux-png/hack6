# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
ans=0
for a in range(N):
    string=input()
    pattern=re.compile(r'hackerrank|HackerRank')
    Ans=pattern.search(string)
    print(Ans)
    if Ans:
        ans+=1
print(ans)
