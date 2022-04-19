 #Enter your code here. Read input from STDIN. Print output to #STDOUT
input()
s1=set(input().split())
s1=set(map(int,s1))
input()
s2=set(input().split())
s2=set(map(int,s2))

Union=s1.union(s2)
Intersection=s1.intersection(s2)


for i in Intersection:
    Union.remove(i)
ls=sorted(Union)


for k in ls :
    print(k)

