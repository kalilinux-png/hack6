import re
list1=[]
N=int(input())
for a in range(N):
    list1.append(input())
code=' '.join(list1)
pattern=re.compile(r'(?<=<)\w+(?=>)*')
ans1=pattern.findall(code)
ans=sorted(set(pattern.findall(code)))
print(*ans,sep=';')
''' OMG THAT SO STUPID IN THIS WHAT MISTAKE I WAS DOING
IS THAT I SORTED THE LIST AND THEN MADE THE SET
SO WHAT HAPPEND IS THE SORTING FAILED '''
''' THANK YOU GOD FOR THIS THING I WILL REMEBER IT'''
''' THANK'S SO MUCH BHAGWAN FOR THIS IMPORTANT
UNIVERSE AND ANSWER'''
