import sys
import re 
pattern=re.compile(r'#[a-fA-F0-9]{3,6}')
N=int(input())
ans=''
try: 
    while N:
        # test=input(
        if '{' in input():
            while N:
                test=input()
                if '}'  in test:
                    # ans+=test
                    break
                else:
                    ans+=test
                N-=1
        N-=1
except EOFError as e:
    pass

print(*pattern.findall(ans),sep='\n')
