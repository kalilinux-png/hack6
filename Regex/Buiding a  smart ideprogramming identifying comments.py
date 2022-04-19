# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
list1=[]
while True:
    string=input()
    if string=='':
        break 
    else:
        list1.append(string)
        continue
string=''.join(list1)
string2=re.sub(r''
pattern=re.compile((r'/\*\w+\*/|//\w+',re.M))
ans=pattern.findall(string)
for a in ans:
    print(a)
