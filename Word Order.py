# this question was done in a fast way
# I think speed of typing is directly proportional to thinking or vice
# versa
''' all thanks to my lord krishna  tumeve mata che petah tumehve
tumheve bandhu cha sakha tumheve
 tumheve vidhya dravin dumheve tumheve
 sarva mam deva he deva'''
from collections import OrderedDict
N=int(input())
od= OrderedDict()
for a in range(N):
    s=input()
    if s in od:
        od[s]=od[s]+1
    else:
        od[s]=1
print(len(set(od)))
for a in od:
    print(od[a],end=' ')
'''let me go and check out for the code chef competation '''
