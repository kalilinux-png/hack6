# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
pattern=re.compile(r'^[4-6][0-9]{3}-{0,1}[0-9]{4}-{0,1}[0-9]{4}-{0,1}[0-9]{4}$')
for a in range(N):
    card_no=input()
    Ans=pattern.search(card_no,)
    # print(Ans)
    if Ans:
        if re.search(r'([0-9])-*\1-*\1-*\1',card_no):
            print('Invalid')
            continue
        print('Valid')
    else:
        print('Invalid')
# Learning : BreakDown the Problem keep calm , be knowledgeful and no wish
