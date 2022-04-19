import re
list1=[]
T=int(input())
for a in range(T):
    list1.append(input())
word_c=int(input())
for c in range(word_c):
    word_find=input()
    ans=re.compile(f'(?<=[\W\D]){word_find}(?=[\W\D])')
    ans1=ans.findall(' '.join(list1))
    print(len(ans1))
