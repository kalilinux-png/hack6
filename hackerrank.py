
s1 = input()
s2 = input()
li = s1.split()
li1 = s2.split()
li=set(map(int,li))
li1=set(map(int,li1))
print(li1)
print(li)
lis=[li.difference(li1),li1.difference(li)]
print(lis.sort(reverse=False))
