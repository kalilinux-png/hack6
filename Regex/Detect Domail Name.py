import re
list1=[]
N=int(input())
for a in range(N):
    list1.append(input())
pattern=re.compile(r'(?<=http://)[\.\w]*')
string=' '.join(list1)
ans=pattern.findall(string)
list2=[]
for c in ans:
    list2.append(c.removeprefix('www.'))
print(*sorted(list2),sep=';')
##''' if this code does not pass all the test cases then then you
##should use group in last where there is a long link
##for ex:http://www.fsfdssf.fsdf.sdffs.sfsdf.fdsfsdf.fs/
##so what you should do is to make a group ans for its one or more
##repetations''''
##''' let me try it out'''
##'''pattern=re.compile(r'http://\w+\.\w+\.\w+\.?[\w]*\.?[\w]+') '''
