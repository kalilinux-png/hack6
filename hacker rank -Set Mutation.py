# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set_element=set(map(int,input().split()))
chance=int(input())
for a in range(chance):
    c,d=input().split()
    d=map(int,input().split())
    if c=='intersection_update':
        set_element.intersection_update(d)
        print(set_element)
    elif c=='update':
        set_element.update(d)
        print(set_element)
    elif c=='symmetric_diffrence_update':
        set_element.symmetric_difference_update(d)
        print(set_element)
    elif c=="diffrence_update":
        set_element.difference_update(d)
        print(set_element)
print(sum(set_element))
