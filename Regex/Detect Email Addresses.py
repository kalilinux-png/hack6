import re
list1=[]
N=int(input())
for a in range(N):
    list1.append(input())
string=' '.join(list1)
pattern=re.compile(r'[\w\.]+@\w+(\.\w+)')
ans=sorted(list(set(pattern.findall(string))))
print(*ans,sep=';')
    
'''
To address the problem, your regex is fine and escaping is
also working well. The issue is that you aren't capturing things correctly.

Let me elaborate upon this. re.findall() returns list of all the
matches or groups found. When you enclose some pattern
within parenthesis as in r'\w+(.\w+)*', you are basically
creating a group. Hence, only the group is returned.
If you enclose it once again like r'(\w+(.\w+)*)', both
groups will be returned as a tuple. Right now you
aren't capturing the complete match at all. Another
better option would be to use non-capturing version
of regular parentheses i.e. (?:...).


Consider the following outputs by re.findall() using different regex for the string name#some.website.co.in to clarify things better :

        Regex                Output by re.findall() 
r'#\w+(\.\w+)*'      ['.in']
r'(#\w+(\.\w+)*)'    [('#some.website.co.in', '.in')]
r'#\w+(?:\.\w+)*'    ['#some.website.co.in']'''
